"""Grant sso-apps users local roles on their municipality root folder.

All the logic lives in ``pas.plugins.kimug.utils.set_sso_apps_local_roles`` so
this thin shim can be dropped, unchanged, into every instance that needs it
(e.g. the directory, events and news buildouts).

Run it (per instance) with::

    bin/instance -O Plone run scripts/set_sso_apps_permissions.py
    bin/instance -O Plone run scripts/set_sso_apps_permissions.py --dry-run

The operation is idempotent (roles are merged, never overwritten) and safe to
re-run. A summary is logged listing granted folders, users with no ``pl_``
group, municipality slugs with no matching root folder, and users missing from
Plone.
"""
from pas.plugins.kimug.utils import get_portal_from_zope_app
from pas.plugins.kimug.utils import set_sso_apps_local_roles

import argparse


parser = argparse.ArgumentParser(description="Grant sso-apps users local roles")
parser.add_argument("-c")  # swallowed by `bin/instance run`
parser.add_argument(
    "--dry-run",
    action="store_true",
    help="Only report what would change; do not set local roles or commit.",
)


if __name__ == "__main__":
    args, _ = parser.parse_known_args()
    portal = get_portal_from_zope_app(app)  # noqa: F821
    set_sso_apps_local_roles(portal, dry_run=args.dry_run)
