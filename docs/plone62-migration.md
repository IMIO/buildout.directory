# Migrating Directory to Plone 6.2.3

Tracks the move of Directory (branch `plone62`, WEB-4533) to Plone 6.2.3 and
Python 3.14. Most of the work is shared with SmartWeb: this buildout extends
the `plone62` pins and sources of buildout.smartweb, and the packages leave
old-style namespace packages (PEP 420) the way the
[SmartWeb migration guide](https://github.com/IMIO/buildout.smartweb/blob/plone62/docs/native-namespaces-migration.md)
describes. This page covers only what is specific to Directory: the packages
it checks out, what changed in this repository, and what's left before
`plone62` can be merged into `main`.

Last updated: 2026-11-24.

## Status

**17 packages**: **10 done** (released, pinned, no longer checked out) · **4
released and pinned**, still checked out by `dev.cfg` (imio.directory.core,
imio.directory.policy, imio.smartweb.common, pas.plugins.kimug) · **1
merged**, not released · **1 PR open** · **1 branch pushed**, no PR yet

✅ done · ⬜ to do · ➖ not applicable · 🚧 its pinned release calls
`pkg_resources` and fails on Plone 6.2.3

| Package | Checked out by | Branch | PR | Merged | Released | Pinned |
|---|:-:|:-:|:-:|:-:|:-:|:-:|
| [imio.helpers](https://github.com/IMIO/buildout.smartweb/blob/plone62/docs/native-namespaces-packages.md#imiohelpers) 🚧 | dev, prod | `plone62` | ⬜ | ⬜ | ⬜ | ⬜ |
| [imio.pyutils](https://github.com/IMIO/buildout.smartweb/blob/plone62/docs/native-namespaces-packages.md#imiopyutils) | dev, prod | `master` | [#4](https://github.com/IMIO/imio.pyutils/pull/4) | ✅ | ⬜ | ⬜ |
| [collective.exportimport](https://github.com/IMIO/buildout.smartweb/blob/plone62/docs/native-namespaces-packages.md#collectiveexportimport) 🚧 | dev, prod | `plone62` | [#287](https://github.com/collective/collective.exportimport/pull/287) (draft) | ⬜ | ⬜ | ⬜ |
| [collective.autopublishing](https://github.com/IMIO/buildout.smartweb/blob/plone62/docs/native-namespaces-packages.md#collectiveautopublishing) | ➖ | ➖ | [#12](https://github.com/collective/collective.autopublishing/pull/12) | ✅ | 2.0.0 | ✅ |
| [collective.behavior.talcondition](https://github.com/IMIO/buildout.smartweb/blob/plone62/docs/native-namespaces-packages.md#collectivebehaviortalcondition) | ➖ | ➖ | [#17](https://github.com/collective/collective.behavior.talcondition/pull/17) | ✅ | 2.0.0 | ✅ |
| [collective.fingerpointing](https://github.com/IMIO/buildout.smartweb/blob/plone62/docs/native-namespaces-packages.md#collectivefingerpointing) | ➖ | ➖ | [#110](https://github.com/collective/collective.fingerpointing/pull/110) | ✅ | 2.0.0 | ✅ |
| [collective.messagesviewlet](https://github.com/IMIO/buildout.smartweb/blob/plone62/docs/native-namespaces-packages.md#collectivemessagesviewlet) | ➖ | ➖ | [#24](https://github.com/collective/collective.messagesviewlet/pull/24) | ✅ | 2.0.0 | ✅ |
| [collective.privacy](https://github.com/IMIO/buildout.smartweb/blob/plone62/docs/native-namespaces-packages.md#collectiveprivacy) | ➖ | ➖ | [#22](https://github.com/collective/collective.privacy/pull/22) | ✅ | 2.0.0 | ✅ |
| [collective.schedulefield](#collectiveschedulefield) | ➖ | ➖ | [#6](https://github.com/IMIO/collective.schedulefield/pull/6) | ✅ | 2.0.0 | ✅ |
| [collective.timedevents](https://github.com/IMIO/buildout.smartweb/blob/plone62/docs/native-namespaces-packages.md#collectivetimedevents) | ➖ | ➖ | [#13](https://github.com/collective/collective.timedevents/pull/13) | ✅ | 2.0.0 | ✅ |
| [collective.upgrade](https://github.com/IMIO/buildout.smartweb/blob/plone62/docs/native-namespaces-packages.md#collectiveupgrade) | ➖ | ➖ | [#20](https://github.com/collective/collective.upgrade/pull/20) | ✅ | 3.0.0 | ✅ |
| [imio.gdpr](https://github.com/IMIO/buildout.smartweb/blob/plone62/docs/native-namespaces-packages.md#imiogdpr) | ➖ | ➖ | [#5](https://github.com/IMIO/imio.gdpr/pull/5) | ✅ | 2.0.0 | ✅ |
| [imio.smartweb.locales](https://github.com/IMIO/buildout.smartweb/blob/plone62/docs/native-namespaces-packages.md#imiosmartwebcommon-core-locales-policy) | ➖ | ➖ | [#4](https://github.com/IMIO/imio.smartweb.locales/pull/4) | ✅ | 2.0.0 | ✅ |
| [imio.directory.core](#imiodirectorycore-and-imiodirectorypolicy) | dev | `main` | [#18](https://github.com/IMIO/imio.directory.core/pull/18) | ✅ | 2.0.0 | ✅ |
| [imio.directory.policy](#imiodirectorycore-and-imiodirectorypolicy) 🚧 | dev | `main` | [#8](https://github.com/IMIO/imio.directory.policy/pull/8) | ✅ | 2.0.0 (old-style) | ✅ |
| [imio.smartweb.common](https://github.com/IMIO/buildout.smartweb/blob/plone62/docs/native-namespaces-packages.md#imiosmartwebcommon-core-locales-policy) | dev | `main` | [#37](https://github.com/IMIO/imio.smartweb.common/pull/37) | ✅ | 2.0.0 | ✅ |
| [pas.plugins.kimug](https://github.com/IMIO/buildout.smartweb/blob/plone62/docs/native-namespaces-packages.md#paspluginskimug) | dev | `main` | [#34](https://github.com/IMIO/pas.plugins.kimug/pull/34) | ✅ | 2.0.0 | ✅ |

Columns:

- **Checked out by**: the `auto-checkout` of `dev.cfg` (dev) and `prod.cfg`
  (prod, so the Docker image). A package checked out by prod only runs as a
  release on a dev instance, and one checked out by dev only runs as its
  pinned release in the image. ➖: not checked out (no longer, or never), the
  pinned release is used.
- **Branch**: the branch mr.developer checks out. It comes from this
  repository's `sources.cfg` for imio.directory.core, imio.directory.policy
  and pas.plugins.kimug, and from buildout.smartweb's `sources.cfg` for the
  others. ➖: not checked out.
- **PR**: the pull request that merges the native branch. ⬜: none opened yet.
- **Released**: the native version on PyPI. **Pinned**: a `versions.cfg`
  (this one or buildout.smartweb's) pins it.

Each row links to the package's details in the SmartWeb guide, except the
three packages only Directory uses, described below:
[imio.directory.core and imio.directory.policy](#imiodirectorycore-and-imiodirectorypolicy),
and [collective.schedulefield](#collectiveschedulefield).

## What's left

### Open pull requests

- [x] imio.directory.core [#18](https://github.com/IMIO/imio.directory.core/pull/18)
  and imio.directory.policy
  [#8](https://github.com/IMIO/imio.directory.policy/pull/8): merged into
  `main` and released as 2.0.0 (2026-11-20).
- [x] imio.directory.core: 2.0.0 was tagged on `plone62`, then #18 was
  squash-merged. `main` is aligned since
  [`59e8bf9`](https://github.com/IMIO/imio.directory.core/commit/59e8bf9)
  (2.0.1.dev0, 2.0.0 section, Plone 6.2 and Python 3.12 to 3.14
  classifiers). The 2.0.0 wheel on PyPI is native.
- [ ] imio.directory.policy: the 2.0.0 on PyPI is **not** native. The `2.0.0`
  tag points to
  [`32e7280`](https://github.com/IMIO/imio.directory.policy/commit/32e7280),
  a "Preparing release 2.0.0" made on the old `main`, before #8 was merged.
  The release commit on `main` (`be300a6`) has no tag. So the wheel still
  has `src/imio/__init__.py` with `declare_namespace`, an `nspkg.pth`, the
  Plone 6.1 classifier and Python 3.12–3.13 only. It imports on Plone 6.2.3
  only because `base.cfg` loads horse-with-no-namespace. `main` itself is
  right (Plone 6.2, Python 3.12 to 3.14, 2.0.1.dev0): release **2.0.1** from
  `main`, then pin it in `versions.cfg`.
- [ ] imio.directory.core's `base.cfg` (still in 2.0.0) copies the
  `collective.schedulefield` and `vobject` pins, because "buildout.directory
  has no plone62 branch yet". It has one now: extend this repository's
  `versions.cfg` from the `plone62` branch instead. Until then, its tests run
  the old-style collective.schedulefield 1.1, while this repository pins
  2.0.0.
- [x] collective.schedulefield
  [#6](https://github.com/IMIO/collective.schedulefield/pull/6): native
  namespace and plone.meta, Plone 6.2 only on Python 3.10 to 3.14
  ([details](#collectiveschedulefield)). Merged into `master` and released
  as 2.0.0 (2026-11-24).

The PRs of the shared packages are tracked in the
[SmartWeb guide](https://github.com/IMIO/buildout.smartweb/blob/plone62/docs/native-namespaces-migration.md#open-pull-requests).

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
- [x] collective.fingerpointing and collective.privacy: dropped from
  `auto-checkout` (2026-11-20). buildout.smartweb pins their native 2.0.0,
  which no longer calls `pkg_resources`.
- [x] collective.behavior.talcondition: dropped from `auto-checkout`
  (2026-11-20). buildout.smartweb pins its native 2.0.0, and its `plone62`
  branch was deleted once
  [#17](https://github.com/collective/collective.behavior.talcondition/pull/17)
  was merged.
- [x] collective.upgrade: this repository's `sources.cfg` no longer checks it
  out from `plone61` (2026-11-20). It now comes from `master`, the branch
  buildout.smartweb's `sources.cfg` names, which contains `plone61` since
  [#20](https://github.com/collective/collective.upgrade/pull/20) was merged.
- [x] collective.schedulefield: dropped from the `auto-checkout` of
  `base.cfg`, and its line from `sources.cfg` (2026-11-24). `versions.cfg`
  pins the native 2.0.0 in place of 1.1. Its `plone62` branch was deleted
  once [#6](https://github.com/IMIO/collective.schedulefield/pull/6) was
  merged, so mr.developer could no longer clone it.
- [x] collective.autopublishing (`prod.cfg`) and collective.upgrade
  (`dev.cfg` and `prod.cfg`): dropped from `auto-checkout` (2026-11-24).
  buildout.smartweb pins their native 2.0.0 and 3.0.0, and no longer checks
  them out either. On a dev instance whose `src/collective.upgrade` is still
  the old-style `plone61` clone, the first buildout after this change stops
  with `No module named 'collective.recipe'`. The cause is the stale
  `develop-eggs/__editable__.collective_upgrade-*.pth`, which buildout loads
  before it removes it. Run buildout again: it then passes.
- [ ] pas.plugins.kimug: drop it from `dev.cfg`, and its line from
  `sources.cfg`, unless you are working on it. buildout.smartweb pins 2.0.0.
- [ ] Make `dev.cfg` and `prod.cfg` check out the same packages. Today only
  dev checks out pas.plugins.kimug, so a dev instance doesn't run the code
  of the image. imio.directory.core, imio.directory.policy and
  imio.smartweb.common, checked out by dev only, are intended.

### Release

When the Plone 6.2 stack goes to production. A PyPI release can't depend on a
git branch, so the order matters:

- [ ] The shared packages first, in the order of the
  [SmartWeb guide](https://github.com/IMIO/buildout.smartweb/blob/plone62/docs/native-namespaces-migration.md#release).
  imio.smartweb.common, collective.behavior.talcondition,
  collective.autopublishing and collective.upgrade are done: they are
  released and pinned (imio.smartweb.common 2.0.0 in `versions.cfg`, the
  others by buildout.smartweb: 2.0.0, 2.0.0 and 3.0.0).
- [x] collective.schedulefield:
  [#6](https://github.com/IMIO/collective.schedulefield/pull/6) merged into
  `master` and released as 2.0.0 (2026-11-24): it drops Plone 6.0 and 6.1.
- [x] imio.directory.core and imio.directory.policy: 2.0.0 released and
  pinned in `versions.cfg` (2026-11-20). `dev.cfg` still checks them out,
  from `main`.
- [ ] imio.directory.policy 2.0.1 from `main`: the 2.0.0 on PyPI was built
  from the old `main` and is still old-style
  ([details](#open-pull-requests)).
- [x] collective.schedulefield 2.0.0 pinned in `versions.cfg` in place of
  1.1, and no longer checked out (2026-11-24).

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
  4.0.3), opening hours (collective.schedulefield 2.0.0), geolocation, taxonomy
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

collective.fingerpointing and collective.privacy: both now come from the
native 2.0.0 releases that buildout.smartweb pins.

collective.behavior.talcondition: it now comes from the native 2.0.0 release
that buildout.smartweb pins.

collective.autopublishing and collective.upgrade: both now come from the
native releases that buildout.smartweb pins (2.0.0 and 3.0.0). Before that,
collective.upgrade was checked out from `master`, as in buildout.smartweb,
once this repository's `sources.cfg` no longer overrode its branch.

imio.directory.core and imio.directory.policy, from `prod.cfg` only: the
image installs the native 2.0.0, which `versions.cfg` pins in place of
1.2.31 and 1.1.9. A dev instance checks out `main`.

### collective.schedulefield 2.0.0

`versions.cfg` pins the native 2.0.0 in place of 1.1. While
[#6](https://github.com/IMIO/collective.schedulefield/pull/6) was open,
`base.cfg` checked out its `plone62` branch (`dcaeb95`), so a dev instance
and the image ran the same code. That checkout and its `sources.cfg` line are
gone: the branch was deleted once merged.

## imio.directory.core and imio.directory.policy

**Namespaces** `imio`, `imio.directory` · **Repositories**
[IMIO/imio.directory.core](https://github.com/IMIO/imio.directory.core) and
[IMIO/imio.directory.policy](https://github.com/IMIO/imio.directory.policy),
branch `main` · **Variant**
[setup.py](https://github.com/IMIO/buildout.smartweb/blob/plone62/docs/native-namespaces-migration.md#the-migration-recipe)
· **Checked out by** `dev.cfg` · **Older stacks** (Plone 6.1) stay on 1.2.x
and 1.1.x

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

Both are merged into `main`
([#18](https://github.com/IMIO/imio.directory.core/pull/18),
[#8](https://github.com/IMIO/imio.directory.policy/pull/8)) and released as
**2.0.0** on 2026-11-20 (Python 3.12+). `versions.cfg` pins both, so the
image installs the releases.

## collective.schedulefield

**Namespace** `collective` · **Repository**
[IMIO/collective.schedulefield](https://github.com/IMIO/collective.schedulefield),
branch `master` · **Variant**
[plone.meta](https://github.com/IMIO/buildout.smartweb/blob/plone62/docs/native-namespaces-migration.md#variant-plonemeta)
· **Checked out by** none, `versions.cfg` pins 2.0.0 · **Required by**
imio.directory.core (the contact opening hours) · **Older stacks** (Plone
6.0 and 6.1) stay on 1.1

The SmartWeb guide doesn't list it, because SmartWeb doesn't use it: only
imio.directory.core requires it, and only this repository pins it. The 1.1
release that `versions.cfg` pinned before calls `pkg_resources` only in
`collective/__init__.py`, to declare the namespace. horse-with-no-namespace's
stub answers that call, so 1.1 imported on Plone 6.2.3, but it was one of the
old-style packages that keep horse-with-no-namespace in `base.cfg`.

Migrated on 2026-11-24, the same way as pas.plugins.kimug
([#6](https://github.com/IMIO/collective.schedulefield/pull/6), 8 commits on
`plone62`, branched off `master`, squash-merged as
[`b8f5468`](https://github.com/IMIO/collective.schedulefield/commit/b8f5468)):

- PEP 420: `src/collective/__init__.py` is gone, and setuptools finds the
  package itself.
- plone.meta 2.12.0: tox, prek and the GitHub workflows. The test matrix runs
  on Plone 6.2.3 with Python 3.10 to 3.14 (the CI runs 3.14 and 3.10). No
  `circular` job: pytest-plone requires `Products.CMFPlone[test]`, which
  depends back on CMFPlone.
- The metadata moved to `pyproject.toml`: SPDX `GPL-2.0-only`, a
  `plone.autoinclude.plugin` entry point, and `plone.api` in the `test`
  extra. The `dev` extra is gone.
- Development environment: uv with Plone 6.2.3 on Python 3.14 (`make install`),
  instead of the Plone 6.1 buildout. `LICENSE.rst` became `LICENSE.md`, and
  the empty `collectiveschedulefield_default.txt` is gone.
- Classifiers: Plone 6.2 only, Python 3.10 to 3.14.

Local checks on 2026-11-24: lint, the 15 tests on Python 3.14 and 3.10,
dependencies and release-check pass. `make start` serves Plone 6.2.3, and
the wheel contains no namespace marker. A buildout of this repository cloned
the branch, and no longer listed it among the old-style namespace packages.

Released as **2.0.0** on 2026-11-24, from
[`0abcfdf`](https://github.com/IMIO/collective.schedulefield/commit/0abcfdf)
on `master`. The wheel on PyPI is native: no `collective/__init__.py`, no
`nspkg.pth` and no `pkg_resources` call. It requires only `Plone`, on
Python 3.10 or later.

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

Last run 2026-11-24, on `plone62` with collective.schedulefield,
collective.autopublishing and collective.upgrade no longer checked out (the
image installs 2.0.0, 2.0.0 and 3.0.0, and checks out only
collective.exportimport, imio.helpers and imio.pyutils): 13 passed (the 11
generic checks, no pending upgrade step included, and the 2 Directory
tests).

**On CI**: each push to `plone62` runs `plone62.yml`. It builds the image
once as `:{short_sha}`, tests it with `tests.yml`, scans it with trivy, and
tags it `:plone62` only if the tests pass. Nothing is deployed. See
[the CI/CD workflows](../.github/workflows/README.md#plone62yml--publish-and-test-plone62-image).
