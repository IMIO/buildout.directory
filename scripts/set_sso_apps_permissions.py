# -*- coding: utf-8 -*-
"""Grant sso-apps users local roles on their municipality root folder.

For every Keycloak sso-apps user that holds the configured access group
(SSO_APPS_ACCESS_GROUP), this script reads their ``pl_<localite>`` groups and,
when a Plone root object exists with id exactly ``<localite>``, grants the user
the Contributor/Editor/Reader local roles on that folder.

Run it (per instance, e.g. on the events and news instances) with::

    bin/instance -O Plone run scripts/set_sso_apps_permissions.py
    bin/instance -O Plone run scripts/set_sso_apps_permissions.py --dry-run

The script is idempotent (roles are merged, never overwritten) and safe to re-run.
A summary report lists granted folders, users with no ``pl_`` group, municipality
slugs with no matching root folder, and users missing from Plone.
"""
from AccessControl.SecurityManagement import newSecurityManager
from pas.plugins.kimug.utils import get_sso_apps_users_with_municipalities
from plone import api
from Products.CMFPlone.interfaces.siteroot import IPloneSiteRoot
from Testing import makerequest
from zope.component.hooks import setSite
from zope.globalrequest import setRequest

import argparse
import logging
import sys


logger = logging.getLogger("set_sso_apps_permissions")
logger.setLevel(logging.INFO)
_handler = logging.StreamHandler(sys.stdout)
_handler.setLevel(logging.INFO)
_handler.setFormatter(
    logging.Formatter(
        "%(asctime)s %(levelname)s %(name)s %(message)s", "%Y-%m-%d %H:%M:%S"
    )
)
logger.addHandler(_handler)

LOCAL_ROLES = ("Contributor", "Editor", "Reader")

parser = argparse.ArgumentParser(description="Grant sso-apps users local roles")
parser.add_argument("-c")  # swallowed by `bin/instance run`
parser.add_argument(
    "--dry-run",
    action="store_true",
    help="Only report what would change; do not set local roles or commit.",
)


def get_site():
    zopeapp = makerequest.makerequest(app)  # noqa: F821
    zopeapp.REQUEST["PARENTS"] = [app]  # noqa: F821
    setRequest(zopeapp.REQUEST)
    user = app.acl_users.getUser("admin")  # noqa: F821
    newSecurityManager(None, user.__of__(app.acl_users))  # noqa: F821
    portal = None
    for oid in app.objectIds():  # noqa: F821
        obj = app[oid]  # noqa: F821
        if IPloneSiteRoot.providedBy(obj):
            portal = obj
            break
    if not portal:
        raise Exception("Can't find portal !")
    setSite(portal)
    return portal


def _resolve_userid(user):
    """Return the Plone userid for an sso-apps user, or None if absent in Plone.

    sso-apps users are created with their keycloak_id as the Plone userid
    (see add_keycloak_users_to_plone / oidc._create_user), but resolve via the
    username first so we use whatever id Plone actually stored.
    """
    member = api.user.get(username=user.get("username"))
    if member is not None:
        return member.getId()
    keycloak_id = user.get("keycloak_id")
    if keycloak_id and api.user.get(userid=keycloak_id) is not None:
        return keycloak_id
    return None


def set_permissions(portal, dry_run=False):
    users = get_sso_apps_users_with_municipalities()
    logger.info(f"Fetched {len(users)} sso-apps users from Keycloak")
    root_ids = set(portal.objectIds())

    granted = []  # (username, userid, localite)
    no_group = []  # username
    no_folder = []  # (username, localite)
    missing_user = []  # username

    for user in users:
        username = user.get("username")
        userid = _resolve_userid(user)
        if userid is None:
            missing_user.append(username)
            logger.warning(f"User '{username}' not found in Plone, skipping")
            continue

        municipalities = user.get("municipalities") or []
        if not municipalities:
            no_group.append(username)
            continue

        for localite in municipalities:
            if localite not in root_ids:
                no_folder.append((username, localite))
                continue
            folder = portal[localite]
            current = set(folder.get_local_roles_for_userid(userid))
            new_roles = sorted(current | set(LOCAL_ROLES))
            if not dry_run:
                folder.manage_setLocalRoles(userid, new_roles)
                folder.reindexObjectSecurity()
            granted.append((username, userid, localite))
            logger.info(
                f"{'[dry-run] would grant' if dry_run else 'Granted'} "
                f"{list(LOCAL_ROLES)} to '{username}' ({userid}) on /{localite}"
            )

    logger.info("=== Summary ===")
    logger.info(f"Granted on a folder : {len(granted)}")
    logger.info(f"Users without pl_ group : {len(no_group)} -> {sorted(no_group)}")
    logger.info(
        f"Municipality slugs without matching root folder : {len(no_folder)} -> "
        f"{sorted(no_folder)}"
    )
    logger.info(
        f"Users missing in Plone : {len(missing_user)} -> {sorted(missing_user)}"
    )

    if not dry_run:
        import transaction

        transaction.commit()
        logger.info("Transaction committed")
    else:
        logger.info("Dry-run: no changes committed")


if __name__ == "__main__":
    args, _ = parser.parse_known_args()
    portal = get_site()
    set_permissions(portal, dry_run=args.dry_run)
