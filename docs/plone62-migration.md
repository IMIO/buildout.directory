# Migrating Directory to Plone 6.2.3

Tracks the move of Directory (branch `plone62`, WEB-4533) to Plone 6.2.3 and
Python 3.14. Most of the work is shared with SmartWeb: this buildout extends
the `plone62` pins and sources of buildout.smartweb, and the packages leave
old-style namespace packages (PEP 420) the way the
[SmartWeb migration guide](https://github.com/IMIO/buildout.smartweb/blob/plone62/docs/native-namespaces-migration.md)
describes. This page covers only what is specific to Directory: the packages
it checks out, what changed in this repository, and what's left before
`plone62` can be merged into `main`.

Last updated: 2026-11-19.

## Status

**17 packages**: **4 done** (released, pinned, no longer checked out) · **2
released and pinned**, still checked out by `dev.cfg` (imio.smartweb.common,
pas.plugins.kimug) · **2 merged**, not released · **4 PRs open** · **4
branches pushed**, no PR yet · **1 not started** (collective.schedulefield: still old-style, doesn't block
Plone 6.2.3)

✅ done · ⬜ to do · ➖ not applicable · 🚧 its pinned release calls
`pkg_resources` and fails on Plone 6.2.3

| Package | Checked out by | Branch | PR | Merged | Released | Pinned |
|---|:-:|:-:|:-:|:-:|:-:|:-:|
| [imio.directory.core](#imiodirectorycore-and-imiodirectorypolicy) | dev, prod | `plone62` | ⬜ | ⬜ | ⬜ | ⬜ |
| [imio.directory.policy](#imiodirectorycore-and-imiodirectorypolicy) | dev, prod | `plone62` | ⬜ | ⬜ | ⬜ | ⬜ |
| [imio.helpers](https://github.com/IMIO/buildout.smartweb/blob/plone62/docs/native-namespaces-packages.md#imiohelpers) 🚧 | dev, prod | `plone62` | ⬜ | ⬜ | ⬜ | ⬜ |
| [imio.pyutils](https://github.com/IMIO/buildout.smartweb/blob/plone62/docs/native-namespaces-packages.md#imiopyutils) | dev, prod | `master` | [#4](https://github.com/IMIO/imio.pyutils/pull/4) | ✅ | ⬜ | ⬜ |
| [collective.autopublishing](https://github.com/IMIO/buildout.smartweb/blob/plone62/docs/native-namespaces-packages.md#collectiveautopublishing) | prod | `plone62` | [#12](https://github.com/collective/collective.autopublishing/pull/12) | ⬜ | ⬜ | ⬜ |
| [collective.behavior.talcondition](https://github.com/IMIO/buildout.smartweb/blob/plone62/docs/native-namespaces-packages.md#collectivebehaviortalcondition) | dev, prod | `plone62` | ⬜ | ⬜ | ⬜ | ⬜ |
| [collective.exportimport](https://github.com/IMIO/buildout.smartweb/blob/plone62/docs/native-namespaces-packages.md#collectiveexportimport) 🚧 | dev, prod | `plone62` | [#287](https://github.com/collective/collective.exportimport/pull/287) (draft) | ⬜ | ⬜ | ⬜ |
| [collective.fingerpointing](https://github.com/IMIO/buildout.smartweb/blob/plone62/docs/native-namespaces-packages.md#collectivefingerpointing) 🚧 | dev, prod | `master` | [#110](https://github.com/collective/collective.fingerpointing/pull/110) | ✅ | ⬜ | ⬜ |
| [collective.privacy](https://github.com/IMIO/buildout.smartweb/blob/plone62/docs/native-namespaces-packages.md#collectiveprivacy) 🚧 | dev, prod | `plone62` | [#22](https://github.com/collective/collective.privacy/pull/22) | ⬜ | ⬜ | ⬜ |
| [collective.schedulefield](#collectiveschedulefield) | ➖ | ➖ | ⬜ | ⬜ | ⬜ | ⬜ |
| [collective.upgrade](https://github.com/IMIO/buildout.smartweb/blob/plone62/docs/native-namespaces-packages.md#collectiveupgrade) | dev, prod | `plone61` | [#20](https://github.com/collective/collective.upgrade/pull/20) | ⬜ | ⬜ | ➖ |
| [collective.messagesviewlet](https://github.com/IMIO/buildout.smartweb/blob/plone62/docs/native-namespaces-packages.md#collectivemessagesviewlet) | ➖ | ➖ | [#24](https://github.com/collective/collective.messagesviewlet/pull/24) | ✅ | 2.0.0 | ✅ |
| [collective.timedevents](https://github.com/IMIO/buildout.smartweb/blob/plone62/docs/native-namespaces-packages.md#collectivetimedevents) | ➖ | ➖ | [#13](https://github.com/collective/collective.timedevents/pull/13) | ✅ | 2.0.0 | ✅ |
| [imio.gdpr](https://github.com/IMIO/buildout.smartweb/blob/plone62/docs/native-namespaces-packages.md#imiogdpr) | ➖ | ➖ | [#5](https://github.com/IMIO/imio.gdpr/pull/5) | ✅ | 2.0.0 | ✅ |
| [imio.smartweb.locales](https://github.com/IMIO/buildout.smartweb/blob/plone62/docs/native-namespaces-packages.md#imiosmartwebcommon-core-locales-policy) | ➖ | ➖ | [#4](https://github.com/IMIO/imio.smartweb.locales/pull/4) | ✅ | 2.0.0 | ✅ |
| [imio.smartweb.common](https://github.com/IMIO/buildout.smartweb/blob/plone62/docs/native-namespaces-packages.md#imiosmartwebcommon-core-locales-policy) | dev | `main` | [#37](https://github.com/IMIO/imio.smartweb.common/pull/37) | ✅ | 2.0.0 | ✅ |
| [pas.plugins.kimug](https://github.com/IMIO/buildout.smartweb/blob/plone62/docs/native-namespaces-packages.md#paspluginskimug) | dev | `main` | [#34](https://github.com/IMIO/pas.plugins.kimug/pull/34) | ✅ | 2.0.0 | ✅ |

Columns:

- **Checked out by**: the `auto-checkout` of `dev.cfg` (dev) and `prod.cfg`
  (prod, so the Docker image). A package checked out by prod only runs as a
  release on a dev instance, and one checked out by dev only runs as its
  pinned release in the image. ➖: not checked out (no longer, or never), the
  pinned release is used.
- **Branch**: the branch mr.developer checks out. It comes from this
  repository's `sources.cfg` for imio.directory.core, imio.directory.policy,
  collective.upgrade and pas.plugins.kimug, and from buildout.smartweb's
  `sources.cfg` for the others. ➖: not checked out.
- **PR**: the pull request that merges the native branch. ⬜: none opened yet.
- **Released**: the native version on PyPI. **Pinned**: a `versions.cfg`
  (this one or buildout.smartweb's) pins it. ➖: collective.upgrade is never
  pinned, every config checks it out.

Each row links to the package's details in the SmartWeb guide, except the
three packages only Directory uses, described below:
[imio.directory.core and imio.directory.policy](#imiodirectorycore-and-imiodirectorypolicy),
and [collective.schedulefield](#collectiveschedulefield).

## What's left

### Open pull requests

- [ ] imio.directory.core: merge `main` into `plone62` first. `main` has
  released 1.2.31 since the branch was made, and the branch's `CHANGES.rst`
  still lists its PEP 420 entry under "1.2.31 (unreleased)".
- [ ] imio.directory.core and imio.directory.policy: `plone62` into `main`.
- [ ] Their `base.cfg` copy the `collective.schedulefield` and `vobject` pins,
  and imio.directory.policy's checks out imio.directory.core in a `[sources]`
  section of its own, because "buildout.directory has no plone62 branch
  yet". It has one now: extend this repository's `versions.cfg` and
  `sources.cfg` from the `plone62` branch instead.

The PRs of the shared packages are tracked in the
[SmartWeb guide](https://github.com/IMIO/buildout.smartweb/blob/plone62/docs/native-namespaces-migration.md#open-pull-requests).

### Not started

- [ ] collective.schedulefield: still old-style
  ([details](#collectiveschedulefield)). It doesn't block Plone 6.2.3, but
  it is one of the old-style packages that keep horse-with-no-namespace in
  `base.cfg`. IMIO owns the repository, so there is no upstream to wait for:
  branch `plone62` off `master`, apply the
  [migration recipe](https://github.com/IMIO/buildout.smartweb/blob/plone62/docs/native-namespaces-migration.md#the-migration-recipe)
  (setup.py variant), and open a PR.

### Clean up the checkouts

- [x] collective.messagesviewlet: dropped from `prod.cfg` (2026-11-19).
  `prod.cfg` checked it out from `plone62`, the branch buildout.smartweb's
  `sources.cfg` names, which was deleted once
  [#24](https://github.com/collective/collective.messagesviewlet/pull/24) was
  merged. mr.developer couldn't clone it, so the image no longer built. The
  image now installs the native 2.0.0 that buildout.smartweb pins.
- [x] imio.smartweb.locales: dropped from `auto-checkout`, and
  `imio.smartweb.locales = 1.1.32` removed from `versions.cfg`, in the same
  commit (2026-11-19). `versions.cfg` is extended last, so its 1.1.32
  (old-style) overrode the 2.0.0 that buildout.smartweb pins: the checkout
  only hid it.
- [x] collective.timedevents and imio.gdpr: dropped from `auto-checkout`
  (2026-11-19). buildout.smartweb pins their native 2.0.0.
- [x] imio.smartweb.common: dropped from `prod.cfg` and from this
  repository's `sources.cfg` (2026-11-19). Its `plone62` branch was deleted
  once [#37](https://github.com/IMIO/imio.smartweb.common/pull/37) was
  merged. `versions.cfg` pins 2.0.0 in place of 1.2.65, so the image
  installs the release. `dev.cfg` still checks it out, from `main` now (the
  branch buildout.smartweb's `sources.cfg` names), as on this repository's
  `main`.
- [ ] pas.plugins.kimug: drop it from `dev.cfg`, and its line from
  `sources.cfg`, unless you are working on it. buildout.smartweb pins 2.0.0.
- [ ] Make `dev.cfg` and `prod.cfg` check out the same packages. Today only
  prod checks out collective.autopublishing, and only dev checks out
  pas.plugins.kimug, so a dev instance doesn't run the code of the image.
  imio.smartweb.common, checked out by dev only, is intended.

### Release

When the Plone 6.2 stack goes to production. A PyPI release can't depend on a
git branch, so the order matters:

- [ ] The shared packages first, in the order of the
  [SmartWeb guide](https://github.com/IMIO/buildout.smartweb/blob/plone62/docs/native-namespaces-migration.md#release).
  imio.smartweb.common is done: 2.0.0 is released and pinned in
  `versions.cfg`.
- [ ] collective.schedulefield, as 2.0.0: it drops Plone 6.0 and 6.1.
- [ ] imio.directory.core, then imio.directory.policy (it requires
  imio.directory.core). Release them as 2.0.0, as the SmartWeb guide does
  for the other packages: they drop Plone 6.1. Their `CHANGES.rst` still says
  1.2.31 (already released from `main`) and 1.1.10.
- [ ] Pin each native release in `versions.cfg`, replacing the old-style
  pins (imio.directory.core 1.2.31, imio.directory.policy 1.1.9,
  collective.schedulefield 1.1). Then drop the checkouts and their
  `sources.cfg` lines.

### Check by hand on a Directory site

- [ ] Search, and the indexing of a new contact: collective.solr goes from
  9.4.0 to 11.0.0.dev0
  ([details](https://github.com/IMIO/buildout.smartweb/blob/plone62/docs/native-namespaces-packages.md#collectivesolr)).
  Check the `directory` core of the production Solr too.
- [ ] The `@search` endpoint with `selected_entities`, as imio.smartweb.core
  calls it: its RAM cache and `Last-Modified` header.
- [ ] The faceted contact views and their map: change a filter and check that
  the markers follow the results
  ([details](https://github.com/IMIO/buildout.smartweb/blob/plone62/docs/plone-formwidget-geolocation.md)).
- [ ] The contact add and edit forms: phones, mails and URLs (datagridfield
  4.0.3), opening hours (collective.schedulefield), geolocation, taxonomy
  (`contact_category`).
- [ ] collective.exportimport: plone.restapi 10.2.1, which Plone 6.2.3 pins,
  drops every image and file it imports. Wait for plone.restapi 10.3.1
  ([details](https://github.com/IMIO/buildout.smartweb/blob/plone62/docs/native-namespaces-migration.md#fix-upstream)).
- [ ] `make upgrade-steps` on a copy of the production database: no step left
  pending.
- [ ] Health probes on port 8081 (`/live`, `/ready`, `/startup`) and
  `@@metrics`.

### When `plone62` is merged into `main`

- [ ] `base.cfg`: extend buildout.smartweb's `main` again (once its own
  `plone62` is merged).
- [ ] `sources.cfg`: back to `main`/`master`, or the lines dropped once the
  packages are released.
- [ ] `tests/docker-compose.test.yml`: fetch the Solr configuration from
  buildout.smartweb's `main`.
- [ ] Delete `.github/workflows/plone62.yml` and its section in
  `.github/workflows/README.md`.
- [ ] `dev.yml` and `staging.yml`: test the image before tagging it, as
  `plone62.yml` does, so a failing image never gets the `:dev` or `:staging`
  tag.

## What changed in buildout.directory

### Plone 6.2.3 (`38534ac`)

- `base.cfg` extends the Plone 6.2.3 pins, and buildout.smartweb's `plone62`
  `versions.cfg` and `sources.cfg`. Products.PloneHotfix20261110 is no longer
  installed.
- `requirements.txt` only includes Plone 6.2.3's requirements: the security
  advisory pins (plone.autoform, plone.restapi, plone.app.content, pip,
  certifi) are gone. `versions.cfg` no longer pins plone.restapi 9.14.0.
- `sources.cfg` checks out imio.directory.core, imio.directory.policy and
  imio.smartweb.common from their `plone62` branch. The
  collective.z3cform.datagridfield checkout is gone: its fix is in 4.0.3.
- `dev.cfg` and `prod.cfg` check out the packages whose releases still call
  `pkg_resources` ([Status](#status)).
- Dockerfile: base image `plone-base:6.2.3` with Python 3.14, pip 26.3,
  zc.buildout 6.0.2, setuptools 84.2.1 and wheel 0.48.0. Debian packages
  renamed in the new base image: `libpcre3-dev` → `libpcre2-dev`,
  `libmemcached11` → `libmemcached11t64`, `libxml2` → `libxml2-16`.

### plone.observability (`fbf18f6`)

The same WSGI pipeline as buildout.smartweb: health probes on port 8081
(`/live`, `/ready`, `/startup`), the `@@metrics` endpoint and OpenTelemetry
tracing, inactive until `OTEL_EXPORTER_OTLP_ENDPOINT` is set.

### Image tests and CI

As in buildout.smartweb and buildout.events: `make test`, `tests/`, and the
`tests.yml` and `plone62.yml` workflows ([Testing](#testing)).

### Checkouts dropped

collective.messagesviewlet (its branch was gone, so the image no longer
built), imio.smartweb.locales with its 1.1.32 pin, collective.timedevents and
imio.gdpr. All four now come from the native 2.0.0 releases that
buildout.smartweb pins.

imio.smartweb.common, from `prod.cfg` only: its `plone62` branch was gone
too. The image installs the native 2.0.0, which `versions.cfg` pins in place
of 1.2.65. A dev instance checks out `main`
([details](#clean-up-the-checkouts)).

## imio.directory.core and imio.directory.policy

**Namespaces** `imio`, `imio.directory` · **Repositories**
[IMIO/imio.directory.core](https://github.com/IMIO/imio.directory.core) and
[IMIO/imio.directory.policy](https://github.com/IMIO/imio.directory.policy),
branch `plone62` · **Variant**
[setup.py](https://github.com/IMIO/buildout.smartweb/blob/plone62/docs/native-namespaces-migration.md#the-migration-recipe)
· **Checked out by** `dev.cfg`, `prod.cfg` · **Older stacks** (Plone 6.1)
stay on 1.2.x and 1.1.x

Migrated by a colleague on 2026-11-17 and 2026-11-18. Each branch is 3
commits ahead of `main`; imio.directory.core's is also 2 commits behind (the
1.2.31 release):

- PEP 420: `namespace_packages` and the namespace files
  (`src/imio/__init__.py`, `src/imio/directory/__init__.py`) are gone, and
  setuptools finds the packages itself.
- Their `base.cfg` extends Plone 6.2.3 and buildout.smartweb's `plone62`, and
  checks out the packages whose releases call `pkg_resources` (imio.helpers,
  collective.behavior.talcondition, collective.privacy, and
  collective.timedevents for the policy).
- Classifiers: Plone 6.2 only, and Python 3.14, which the CI matrix now tests.

## collective.schedulefield

**Namespace** `collective` · **Repository**
[IMIO/collective.schedulefield](https://github.com/IMIO/collective.schedulefield),
branch `master` · **Variant**
[setup.py](https://github.com/IMIO/buildout.smartweb/blob/plone62/docs/native-namespaces-migration.md#the-migration-recipe)
· **Checked out by** none · **Required by** imio.directory.core (the contact
opening hours)

Not started: still old-style, but it doesn't block Plone 6.2.3.

- The 1.1 release that `versions.cfg` pins calls `pkg_resources` only in
  `collective/__init__.py`, to declare the namespace. horse-with-no-namespace's
  stub answers that call, so 1.1 imports on Plone 6.2.3 and nothing forced a
  checkout.
- The SmartWeb guide doesn't list it, because SmartWeb doesn't use it: only
  imio.directory.core requires it, and only this repository pins it.
- `master` is 1.1.1.dev0, still with `namespace_packages=["collective"]` and
  the Plone 6.0 and 6.1 classifiers. There is no `plone62` branch. The last
  merged PR is [#5](https://github.com/IMIO/collective.schedulefield/pull/5)
  (Plone 6.1 compatibility, May 2025).

## Testing

**Locally**: `make test` builds the production image from this checkout
(`prod.cfg`). It boots the image with Postgres 17, memcached and Solr 9.6, and
collective.big.bang creates the site with `imio.directory.policy`. Then it
runs:

- the generic checks of
  [IMIO/gha `plone-image-test-notify`](https://github.com/IMIO/gha/tree/v8/plone-image-test-notify);
- `tests/test_directory.py`: create an entity and a contact and render them,
  and find a new contact with `@search` (through Solr).

The Solr container downloads the `directory` core configuration from
buildout.smartweb when it starts, so the test needs network access.
`tests/log_allowlist.txt` lists the log records that are expected, and why.

Last run 2026-11-19, on `plone62` with the five checkouts above dropped (the
image installs their 2.0.0): 13 passed (the 11 generic checks, no pending
upgrade step included, and the 2 Directory tests).

**On CI**: each push to `plone62` runs `plone62.yml`. It builds the image
once as `:{short_sha}`, tests it with `tests.yml`, scans it with trivy, and
tags it `:plone62` only if the tests pass. Nothing is deployed. See
[the CI/CD workflows](../.github/workflows/README.md#plone62yml--publish-and-test-plone62-image).
