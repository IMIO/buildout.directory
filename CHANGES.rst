1.5.5 (unreleased)
------------------

- Nothing changed yet.


1.5.4 (2025-07-30)
------------------

- imio.directory.core 1.2.23

    - WEB-4265 : Add new terms in facilities vocabulary
      [remdub]

- imio.smartweb.locales 1.1.32

    - Update translations
      [remdub]

- imio.smartweb.locales 1.1.31

    - Add some translations for new smartweb site admin control panel
      [boulch]


1.5.3 (2025-07-24)
------------------

- imio.directory.core 1.2.22

    - WEB-4286 : Fix geolocation for contacts with default coordinates
      [remdub]


1.5.2 (2025-06-25)
------------------

- imio.smartweb.common 1.2.36

    - WEB-4278 : Create translated (de) iam vocabulary for e-guichet (citizen project)
      [boulch]

    - WEB-4278 : Create translated (de) topics vocabulary for e-guichet (citizen project)
      [boulch]

    - WEB-4269 : Add Horizontal Rule option to the insert menu in TinyMCE
      [remdub]

- imio.directory.core 1.2.20

    - WEB-4278 : Create translated (de) contact categories vocabulary for e-guichet (citizen project)
      [boulch]

    - WEB-4278 : Create translated (de) factilities vocabulary for e-guichet (citizen project)
      [boulch]

    - WEB-4278 : Create translated (de) contact types vocabulary for e-guichet (citizen project)
      [boulch]


1.5.1 (2025-05-26)
------------------

- imio.smartweb.common 1.2.35

    - CITI-7 : Fix retrieving mimeType for some picture files
      [boulch]

- imio.smartweb.common 1.2.34

    - WEB-4258 : Temporary CSS fix to unhide the "External link" tab when adding a new link.
      This a temporary fix while waiting for a new release in imio_smartweb_themes
      [remdub]

- imio.smartweb.common 1.2.33

    - WEB-4259 : Override plone.volto summary_serializer_metadata to solve a problem with new
      metadata fields being added to the summary serializer and breaking our search endpoints
      [bsuttor, remdub]

- imio.smartweb.locales 1.1.30

    - WEB-4260 : Override default Plone translation for TinyMCE "Insert link"
      We don't allow to upload files through the TinyMCE editor, so we don't need this
      [remdub]


1.5 (2025-05-20)
----------------

- imio.smartweb.common 1.2.32

    - WEB-4250 : Quick fix : Since Plone 6.1, AjaxSelectWidget is displaying in edit mode even if mode is "display"
      [boulch]

- imio.smartweb.locales 1.1.29

    - Update dev environment to Plone 6.1-latest
      [remdub]

- collective.schedulefield 1.1

    - Update locales https://github.com/IMIO/collective.schedulefield/issues/3
      [remdub]

    - Add test environment using pytest, with test coverage reaching 80% https://github.com/IMIO/collective.schedulefield/issues/2
      [remdub]

    - Fix MultiSchedule viewlet https://github.com/IMIO/collective.schedulefield/issues/4
      [remdub]

    - Upgrade dev environment to Plone 6.1-latest
      [remdub]

- imio.directory.core 1.2.19

    - Upgrade dev environment to Plone 6.1-latest
      [remdub]

    - Add tests for Plone 6.1-latest and add Python 3.13
      [remdub]

- imio.directory.policy 1.1.7

    - GHA tests on Python 3.10 3.11, 3.12 and 3.13
      [remdub]

    - Update Python classifiers to be compatible with Plone 6.1 and Python 3.13
      [remdub]

- imio.directory.policy 1.1.6

    - Update Python classifiers to be compatible with Python 3.12
      [remdub]

    - Migrate to Plone 6.0.14
      [boulch]

- imio.smartweb.common 1.2.31

    - Dirty css fix to hide the "Upload" button in the new pat-contentbrowser
      [remdub]

- imio.smartweb.common 1.2.30

    - Upgrade missing TinyMCE settings to version 7
      [remdub]

- imio.smartweb.common 1.2.29

    - Upgrade TinyMCE settings to version 7
      [remdub]

- imio.smartweb.common 1.2.28

    - Upgrade dev environment to Plone 6.1-latest
      [remdub]

    - Add tests for Plone 6.1-latest and add Python 3.13
      [remdub]

- collective.upgrade (plone61 branch)

    - Portal_properties is no longer a persistent tool (Plone 6.1 compatibility)
      [bsuttor]

- zope.session 5.1

    - Python 3.10, 3.11 compatibility
      For more details, see : https://raw.githubusercontent.com/zopefoundation/zope.session/refs/heads/master/CHANGES.rst

- z3c.unconfigure 2.1

    - Python 3.12, 3.13 compatibility
      For more details, see : https://raw.githubusercontent.com/zopefoundation/z3c.unconfigure/refs/heads/master/CHANGES.rst

- z3c.jbot 2.2

    - Drop support for Python 3.8
      For more details, see : https://raw.githubusercontent.com/zopefoundation/z3c.jbot/refs/heads/master/CHANGES.rst

- RelStorage 4.1.1

    - Python 3.13 compatibility
      For more details, see : https://raw.githubusercontent.com/zodb/relstorage/refs/heads/master/CHANGES.rst

- psycopg2 2.9.10

    - Python 3.13 compatibility
      For more details, see : https://raw.githubusercontent.com/psycopg/psycopg2/refs/heads/master/NEWS

- plone.gallery 1.1.6

    - For more details, see : https://raw.githubusercontent.com/plone/plone.gallery/refs/heads/master/CHANGES.rst

- pas.plugins.authomatic 2.0.0rc3

    - Pinned new version for Plone 6.1 compatibility
      For more details, see : https://raw.githubusercontent.com/collective/pas.plugins.authomatic/refs/heads/main/CHANGELOG.md

- pas.plugins.imio 2.1

    - Plone 6.1 compatibility.
      [remdub]


1.4.9 (2025-03-19)
------------------

- imio.directory.core 1.2.18

    - Update Python classifiers to be compatible with Python 3.12
      [remdub]

    - Migrate to Plone 6.0.14
      [boulch]

- imio.smartweb.common 1.2.27

    - WEB-4122 : Create adapter/validator to filter valid image mimetype in our solutions
      [boulch]

- imio.smartweb.common 1.2.26

    - WEB-4212: Fixe i18n:domain for skip to content
      [thomlamb]

- WEB-4226 : Use waitress instead of gunicorn
  The issue leading to a high load with waitress has been fixed in waitress 3.0.1
  See https://github.com/Pylons/waitress/pull/435
  [remdub]

- imio.smartweb.common 1.2.25

    - WEB-4232 : Fix JQuery.
      Version 1.2.24 contained issues affecting the smooth running of the preventing deletion of a taxonomy term
      [boulch]

- imio.smartweb.common 1.2.24

    - WEB-4232 : Refactoring of the code that prevents the deletion of a taxonomy term if it is used in at least one object
      [boulch]

- imio.smartweb.common 1.2.23

    - WEB-3718 : Accessibility : Add aria-label for consent buttons
      [boulch]


1.4.8 (2025-02-24)
------------------

- imio.smartweb.common 1.2.22

    - WEB-4153 : Ruleset plone.stableResource for image scales
      [remdub]


1.4.7 (2025-02-02)
------------------

- Set event log level to error in production configuration and debug in dev configuration
  [bsuttor]

- imio.smartweb.common 1.2.21

    - Fix: Updated to align scale behavior with the fix in plone.scale ([commit a352815](https://github.com/plone/plone.scale/commit/a352815#diff-24f46fc714c6d36041bcea7e64a7d5aeceacd929eb802655276a1d8f4b4576f4R209))
      [boulch]


1.4.6 (2025-01-29)
------------------

- Migrate to Python 3.12, Plone 6.0.14
  [boulch, remdub]

- z3c.jbot 2.1

    - Fix error when Plone site is not yet set as in first index_html call on Zope
      [bsuttor]


1.4.5 (2025-01-20)
------------------

- imio.directory.policy 1.1.5

  - WEB-4153: Increase caching values
    [remdub]


1.4.4 (2025-01-08)
------------------

- imio.directory.core 1.2.17

  - WEB-4153 : Add a new cacheRuleset to use with our custom rest endpoints
    [remdub]

- imio.directory.policy 1.1.4

  - WEB-4153: Set moderateCaching for imio.directory.core.rest
    [remdub]


1.4.3 (2025-01-07)
------------------

- Increase gunicorn limit_request_line to allow long urls and avoid 400 errors
  [remdub]


1.4.2 (2024-10-14)
------------------

- Sync gunicorn version with Plone 6.0.9
  [remdub]

- imio.directory.core 1.2.16

  - WEB-4027 : Add "Linkedin" as a new type of site term
    [boulch]

  - WEB-4088 : Fix missing include package .rest. we couldn't directly call @odwb endpoints.
    [boulch]


1.4.1 (2024-07-31)
------------------

- WEB-3995 : Bump RelStorage to 4.0.0
  [remdub]

- WEB-3995 : Bump psycopg2 to 2.9.9
  [remdub]

- Upgrade to Zope 5.9
  [remdub]


1.4 (2024-07-02)
----------------

- Upgrade docker image to Ubuntu 22.04
  [remdub]


1.3.10 (2024-07-01)
-------------------

- imio.directory.core 1.2.15

    - WEB-4088 : Add after commit hook to reduce bad image upload to odwb because of the transaction speed
      New contact hasn't time to go from private to published state ?!
      [boulch]

- imio.smartweb.common 1.2.18

    - WEB-4088 : Refactor code for odwb staging availability
      [boulch]

    - GHA tests on Python 3.8 3.9 and 3.10
      [remdub]

- imio.directory.core 1.2.14

    - WEB-4088 : Rename some fields to match with odwb dataset
      [boulch]

    - GHA tests on Python 3.8 3.9 and 3.10
      [remdub]


1.3.9 (2024-06-10)
------------------

- imio.smartweb.common 1.2.17

    - WEB-4113 : Add `TranslatedAjaxSelectFieldWidget` to fix translations of initial
      values in select2 fields
      [laulaz]

- imio.smartweb.common 1.2.16

    - WEB-4107 : Update resource registries modification time (used as ETag) at Zope startup
      [laulaz]


1.3.8 (2024-06-06)
------------------

- imio.directory.core 1.2.13

    - Geocode contact only if longitude and latitude are empty on csv import
      [laulaz, remdub]


1.3.7 (2024-05-30)
------------------

- imio.directory.core 1.2.12

    - Fix upgrade step
      [boulch]

- imio.smartweb.locales 1.1.9 => 1.1.18

    - Add missing FR translations
      [laulaz]

- imio.directory.core 1.2.11

    - WEB-4088 : Add some odwb endpoints (for contacts , for entities)
      Cover use case for sending data in odwb for a staging environment
      [boulch]

    - Fix Topics in SearchableText translated indexes
      [laulaz]

- imio.smartweb.common 1.2.15

    - Fix missing ZCML dependency
      [laulaz]

- imio.smartweb.common 1.2.14

    - Fix bundles: Remove obsolete patterns bundle and fix a previous upgrade for
      eea.facetednavigation
      [laulaz]

    - Fix translate call (was causing incorrect string in .po file)
      [laulaz]

    - Fix translation message string
      [laulaz]

- imio.smartweb.common 1.2.13

    - WEB-4088 : Cover use case for sending data in odwb for a staging environment
      [boulch]

    - Ensure translation of vocabularies when used with `AjaxSelectFieldWidget`
      [laulaz]

    - Remove useless `container_uid` from `search-filters` results
      [laulaz]

    - WEB-3864 : Ensure that a taxonomy term that is deleted is not used anywhere
      [boulch]

    - WEB-3862 : Unpatch (restore original) eea.facetednavigation jquery
      [laulaz]

- imio.smartweb.common 1.2.12

    - WEB-4102 : Add second skip to footer
      [thomlamb]

- imio.smartweb.common 1.2.11

    - WEB-4101 : Fix vocabulary terms translation (for Topics only - for the moment)
      when used with `AjaxSelectFieldWidget`
      [laulaz]

- imio.smartweb.common 1.2.10

    - WEB-4101 : Change Topics field widget to keep value ordering
      [laulaz]

    - WEB-4088 : Implement some odwb utils and generic classes
      [boulch]


1.3.6 (2024-04-14)
------------------

- Update versions of setuptools, wheel, pip, Plone in Dockerfile
  [boulch]

- imio.directory.core 1.2.10

    - WEB-4095 : Use "|" separator instead of "," when exporting contacts to csv file
      [boulch]

- Migrate to Plone 6.0.9
  [boulch]


1.3.5 (2024-03-05)
------------------

- imio.directory.core 1.2.9

    - WEB-4072, WEB-4073 : Enable solr.fields behavior on some content types
      [remdub]

    - WEB-4006 : Exclude some content types from search results
      [remdub]

- collective.solr 9.3.0

    - Add support of https connections
      [remdub]

    - Add french locales
      [remdub]

- collective.solr 9.2.3

    - Add upgrade step for missing stopwords registry entries
      [remdub]

1.3.4 (2024-02-12)
------------------

- imio.directory.core 1.2.8

    - MWEBRCHA-14 : Add view to export contacts to csv file
      [boulch]

- imio.smartweb.common 1.2.9

    - WEB-4064 : Reindex SolR because of changes in schema
      [remdub]

- imio.smartweb.common 1.2.8

    - Fix skip content sr-only
      [thomlamb]

- imio.smartweb.common 1.2.7

    - WEB-4046 : Add css for "Skip to content"
      [thomlamb]

    - WEB-4046 : Add "Skip to content" link for a11y
      [laulaz]

    - WEB-4048 : Put focus on cookies accept button for a11y
      [laulaz]


1.3.3 (2024-02-05)
------------------

- imio.directory.core 1.2.7

    - SUP-34841 : Fix contact serializer when contact hasn't schedule
      [boulch]

- imio.directory.core 1.2.6

    - WEB-4006 : Also reindex solr on SearchableText upgrade step
      [remdub]

- imio.directory.core 1.2.5

    - WEB-4006 : Add mail and phone labels in SearchableText
      [remdub]


1.3.2 (2024-01-29)
------------------

- imio.directory.core 1.2.4

    - WEB-4052 : If no schedule so we set "table_date" to None instead of []
      [boulch]

- imio.directory.core 1.2.3

    - WEB-4041 : Handle new "carre" scale
      [boulch]

    - WEB-4007 : Update contact serializer and use ContactProperties to get well formated schedule and help displaying schedule in REACT directory view
      [boulch]

- imio.smartweb.common 1.2.6

    - WEB-4041 : Add new "carre" scale
      [boulch]

- imio.smartweb.common 1.2.5

    - WEB-4007 : Get ContactProperties out of imio.smartweb.core to also use it in imio.directory.core and 
      simplifying formated schedule displaying in REACT directory view
      [boulch]

    - WEB-4029 : File and Image content types don't have WF so we set effective date equal to created date
      [boulch]

- imio.smartweb.common 1.2.4

    - WEB-3783 : Rebuild url with request.form datas (usefull with react views)
      [boulch]


1.3.1-quick (2023-11-23)
------------------------

- Release to force new docker tag / deploy after incomplete build
  [laulaz]


1.3 (2023-11-22)
----------------

- imio.smartweb.common 1.2.3

    - Improve image compression quality
      [laulaz]
  
    - Change portrait scales dimensions
      [laulaz]
  
- imio.smartweb.common 1.2.2

    - Fix missing values for facilities lists (causing None in REST views filters) See collective/collective.solr#366
      [laulaz]

    - Fix last upgrade steps: when run from command line, we need to adopt admin user to find private objects
      [laulaz]

    - WEB-4003 : Fix missing TextField mimetypes
      [laulaz]

- imio.smartweb.common 1.2.1
    - SUP-33128 : Fix eea.facetednavigation : Hide items with 0 results
      [boulch, laz]

    - Refactor less and js compilation + Add compilations files
      [boulch]

- imio.smartweb.locales 1.1.9
    - WEB-4018 : Add missing French translations (new termes in directory vocabulary)
      [boulch]

- imio.directory.core 1.2.2

    - WEB-4018 : Add three new terms in facitilites vocabulary
      [boulch]

    - Fix missing values for topics / iam lists (causing None in REST views filters) See collective/collective.solr#366
      [laulaz]

- imio.smartweb.locales 1.1.8
    - Add missing French translations
      [laulaz]

- Develop collective.solr to implement https connection DEVOPS-3
  [remdub]

- imio.directory.core 1.2.1

    - Remove logo field from cropping editor
      [laulaz]

- imio.directory.core 1.2

    - WEB-3985 : Use new portrait / paysage scales & logic
      [boulch, laulaz]

    - WEB-3985 : Remove old cropping information when image changes
      [boulch, laulaz]

- imio.smartweb.common 1.2

    - WEB-3985 : New portrait / paysage scales & logic.
      We have re-defined the scales & sizes used in smartweb.
      We let the user crop only 2 big portrait / paysage scales and make the calculation behind the scenes for all
      other smaller scales.
      We also fixed the cropping information clearing on images changes.
      [boulch, laulaz]


1.2.9 (2023-10-25)
------------------

- imio.directory.core 1.1.11

    - MWEBITTA-21 : Add entities subscribing to share all contacts
      [boulch, laulaz]

- imio.smartweb.locales 1.1.7
    - Add missing French translations
      [boulch]

    - Update translations
      [boulch]

- imio.smartweb.locales 1.1.6

    - Add missing French translations (external content section and contact section)
      [boulch]


1.2.8 (2023-10-09)
------------------

- imio.directory.core 1.1.10

    - WEB-3918 : Add missing DE translations for contact_category taxonomy
      [laulaz]

    - Update contact_category taxonomy data to reflect production site data
      [laulaz]

- imio.directory.policy 1.1.3

    - WEB-3954 : Hide cropping action on Image type
      [boulch]

    - Migrate to Plone 6.0.4
      [boulch]

- imio.smartweb.locales 1.1.5

    - Add missing translations [boulch]

- imio.smartweb.locales 1.1.4

    - Add missing French translation (folder_contents properties)
      [laulaz]

    - Migrate to Plone 6.0.4
      [boulch]

- imio.smartweb.common 1.1.9
    - WEB-3974 : Add new registry key (imio.smartweb.common.log) to activate logging in smartweb / auth sources products
      [boulch]

    - Fix AttributeError in case of instance behaviors attributes that are not on all objects
      [boulch]

- imio.smartweb.common 1.1.8

    - WEB-3960 : Clean unhautorized xml chars out of text when added or modified contents Temporary patch.
      Waiting for this fix : plone/plone.app.z3cform#167
      [boulch]

    - WEB-3955 : Authentic sources : Crop view on Image type should not return scales
      [boulch]

- imio.smartweb.common 1.1.7

    - Change banner scale to have infinite height
      [laulaz]

    - Migrate to Plone 6.0.4
      [boulch]


1.2.7 (2023-05-30)
------------------

- imio.directory.core 1.1.9

    - Fix condition when facing `Missing.Value` to avoid traceback in serializer
      [laulaz]

    - WEB-3918 : Add missing DE translations for contact_category taxonomy
      [laulaz]

    - Migrate to Plone 6.0.4
      [boulch]

    - Update contact_category taxonomy data to reflect production site data
      [laulaz]

- Rollback to Zope 5.8 for now because of a bug in POST requests with gunicorn
  [boulch]

- WEB-3781 : Add autopublish script
  [remdub]

- Migrate to Plone 6.0.4
  [boulch]


1.2.6 (2023-04-25)
------------------

- imio.smartweb.common 1.1.6

    - Don't use image_scales metadata anymore (Fix faceted)
      [boulch, laulaz]

    - Update object modification date if cropping was removed/updated
      [boulch, laulaz]

- imio.directory.policy 1.1.2

    - Add module : collective.messagesviewlet
      [boulch]

    - Migrate to Plone 6.0.2
      [boulch]


1.2.5 (2023-04-02)
------------------

- imio.directory.core 1.1.8

    - WEB-3909 : Add upgrade step to fix wrongly stored datagrid fields values
      [laulaz]


1.2.4-quick (2023-03-20)
------------------------

- Push images to prod registry.
  [bsuttor]


1.2.3 (2023-03-19)
------------------

- imio.directory.core 1.1.7

    - Fix non empty fields check after Datagridfield update
      [laulaz]

- imio.directory.core 1.1.6

    - Define non empty fields for choices in contact Datagridfield rows & fix labels
      [laulaz]

- imio.directory.core 1.1.5
    
    - Fix "required field" errors in empty Datagridfield rows
      [laulaz]

- imio.smartweb.common 1.1.5

    - WEB-3862 : Patch (Remove select2) eea.facetednavigation jquery
      [laulaz, boulch]

- Get collective.solr = 9.1.1 from buildout.smartweb/versions.cfg
  [boulch]

- imio.smartweb.locales 1.1.3

    - Add missing French translations (Cirkwi & image dimensions warning)
      [laulaz]

    - Migrate to Plone 6.0.2
      [boulch]

- imio.directory.core 1.1.4

    - Add warning message if images are too small to be cropped
      [laulaz]

    - Migrate to Plone 6.0.2
      [boulch]

- imio.smartweb.common 1.1.4

    - Allow to add portal messages when content images are too small for cropping. This can be done dynamically on a view call with a single line of code: show_warning_for_scales(self.context, self.request)
      [laulaz]

    - Migrate to Plone 6.0.2 [boulch]  


1.2.2-quick (2023-03-08)
------------------------

- Develop collective.solr to fix an issue with image_scales metadata
  [mpeeters]


1.2.1 (2023-03-07)
------------------

- Migrate to Plone 6.0.2
  [boulch]


1.2.0 (2023-02-28)
------------------

- imio.directory.core 1.1.3

    - Avoid auto-appending new lines to Datagrid fields when clicked
      [laulaz]

    - Fix reindex after cut / copy / paste in some cases
      [laulaz]

    - Add DE translations in contact_category taxonomy
      [laulaz]

- imio.smartweb.locales 1.1.2

    - WEB-3848 : Add missing translations
      [boulch]

- imio.smartweb.common 1.1.3

    - WEB-3852 : Fix atom/syndication registry keys
      [boulch]


1.2 (2023-02-20)
----------------

- imio.directory.core 1.1.2

    - Remove unused title_fr and description_fr metadatas
      [laulaz]

    - Remove SearchableText_fr (Solr will use SearchableText for FR)
      [laulaz]

- plone.formwidget.geolocation > fix-geosearch

    - Fix usage of default location from configuration
      [mpeeters]

    - Ensure that the marker is the main marker to fix geosearch
      [mpeeters]

- imio.smartweb.common 1.1.2

    - Call @@consent-json view on navigation root (instead of context)
      [laulaz]

    - Ensure Ajax requests are always uncached
      [laulaz]

- Update to Plone 6.0.0.2
  [laulaz]

- imio.smartweb.locales 1.1

    - Add DE translations (with copied French sentences for now)
      [laulaz]

    - Update buildout to Plone 6.0.0 final
      [laulaz]

- imio.directory.policy 1.1.1

    - Install and configure autopublishing (with 15 min tick subscriber)
      [boulch]

    - Remove obsolete TinyMCE override
      [laulaz]

    - Remove available languages (we don't need them anymore)
      [laulaz]

- imio.directory.core 1.1.1

    - Add taxonomy_contact_category_for_filtering index to allow complex queries
      from smartweb directory views
      [laulaz]

    - Add new descriptions metadatas and SearchableText indexes for multilingual
      [laulaz]

- imio.smartweb.common 1.1.1

    - Allow to choose language for vocabulary term translation
      [laulaz]

    - Use bootstrap dropdown-toggle for fieldsets collapse icon on edit forms
      [laulaz]

    - Fix TinyMCE menu bar and format menu
      [laulaz]

    - Update `widget.pt` override from `plone.app.z3cform.templates`
      [laulaz]

    - Improve monkeypatch to fix TTW resource calling
      [laulaz]

    - Update buildout to get Plone 6.0.0 final
      [laulaz]

- imio.smartweb.common 1.1

    - Add monkeypatch to fix TTW resource calling
      See https://github.com/plone/Products.CMFPlone/issues/3705
      [laulaz]

    - Uninstall collective.js.jqueryui
      [boulch]

    - Remove faceted deprecated bundles
      [boulch]

    - Migrate to Plone 6 : remove dexteritytextindexer, use new simplified
      resources registry, fix TinyMCE configuration and images scales,
      manual minimized js
      [laulaz, boulch]

- imio.directory.policy 1.1

    - Update to Plone 6.0.0 final
      [boulch]

- imio.directory.core 1.1

    - Update to Plone 6.0.0 final
      [boulch]

    - Add eea.faceted.navigable behavior on Entity type
      [laulaz]

- Update to Plone 6.0.0 final
  [boulch]


1.1 (2022-11-22)
----------------

- imio.directory.core 1.0

    - Add multilingual features: New fields, vocabularies translations, restapi serializer
      [laulaz]

- imio.directory.policy 1.0

    - Add available languages to prepare for multilingual
      [laulaz]

    - Update buildout to use Plone 6.0.0a3 packages versions
      [boulch]

- imio.smartweb.locales 1.0.8

    - Add missing French translations (Sendinblue, multilingual)
      [laulaz]

- imio.smartweb.common 1.0.10

    - Ignore batch related query parameters for search-filters endpoint
      [laulaz]

- imio.smartweb.common 1.0.9

    - Add helper method to get language from smartweb REST requests This is needed for multilingual authentic sources
      [laulaz]

    - Allow to translate vocabulary terms titles in search-filters endpoint This is needed for multilingual authentic sources
      [laulaz]

- imio.smartweb.common 1.0.8

    - MWEB-54 : Update TinyMCE : Add non breaking space option
      [boulch]



1.0.10 (2022-10-30)
-------------------

- imio.smartweb.locales 1.0.7

    - Add some directory fields translations
      [boulch]

    - Exclude profiles.zcml from translations
      [laulaz]

- imio.directory.core 1.0a7

    - Fix translation
      [boulch]

    - WEB-3762 : Reorder contact fields to encourage good completion + add some fields descriptions
      [boulch]



1.0.9 (2022-10-23)
------------------

- imio.directory.core 1.0a6

    - WEB-3770 : Force include_items in serializer to True to get files and pictures included in contact
      [boulch]

    - Add eea.faceted.navigable behavior on Entity type
      [laulaz]


1.0.8 (2022-09-06)
------------------

- Blobs are now on filesystem.
  [bsuttor]

- imio.directory.core 1.0a5

    - WEB-3726 : Add subjects (keyword) in SearchableText
      [boulch]


1.0.7-quick (2022-07-18)
------------------------

- Update pas.plugins.imio 2.0.6.
  [bsuttor]


1.0.6-quick (2022-07-14)
------------------------

- imio.directory.core 1.0a4

    - Update contact_category taxonomy data to reflect production site data
      [laulaz]

    - [WEBMIGP5-36] Add new vocabulary terms in imio.directory.vocabulary.SiteTypes (Instagram, Pinterest, Youtube)
      [boulch]

    - It's not allowed to put Images or Files in imio.directory.Entity
      [boulch]

- imio.smartweb.common 1.0.7

    - Add connection link in colophon
      [laulaz]

- imio.smartweb.common 1.0.6

    - Add ban_physicalpath method (taken from policy)
      [boulch, laulaz]

- imio.smartweb.common 1.0.5

    - Refactor rich description to retrieve html on a any description
      (from context or from other ways)
      [boulch]

- imio.smartweb.locales 1.0.6

    - Add Dutch translations files
      [laulaz]

    - Add faceted map translation
      [laulaz]

    - Add propose URLs translations
      [laulaz]

- imio.smartweb.locales 1.0.5

    - Add translation for Agent connection
      [laulaz]

- imio.smartweb.locales 1.0.4

    - Add translations for contact gallery
      [laulaz]

    - Add translations for post-it section
      [laulaz]


1.0.5 (2022-07-13)
------------------

- Update pas.plugins.imio 2.0.5, see https://github.com/IMIO/pas.plugins.imio/blob/2.0.5/CHANGES.rst
  [bsuttor]


1.0.4 (2022-05-03)
------------------

- imio.smartweb.locales 1.0.3

    - Add translation for image upload
      [laulaz]

    - Add translations for new icons
      [laulaz]

- imio.smartweb.locales 1.0.2

    - Add Hero banner related translations
      [laulaz]

- imio.smartweb.locales 1.0.1

    - Add missing translation for Local Manager & lead image portrait mode
      [laulaz]

- imio.smartweb.locales 1.0

    - Change 'minisite' to 'site partenaire' in French
      [laulaz]

    - Add icon field related translations
      [laulaz]

- imio.smartweb.locales 1.0a16

    - Fix translation
      [laulaz]

- imio.smartweb.locales 1.0a15

    - Add new icons translations (e-guichet & shopping)
      [laulaz]

- imio.smartweb.locales 1.0a14

    - Add social network translation
      [laulaz]

- imio.smartweb.locales 1.0a13

    - Add event dates related translations
      [laulaz]

- imio.smartweb.locales 1.0a12

    - Add e_guichet view and taxonomies instance behaviors translations
      [laulaz]

- imio.directory.core 1.0a3

    - Use unique urls for images scales to ease caching
      [boulch]

    - Use common.interfaces.ILocalManagerAware to mark a locally manageable content
      [boulch]

- imio.smartweb.common 1.0.4

    - Limit uploaded files sizes to 20Mo with JS (without reaching the server)
      [laulaz]

    - Add help text on lead image field also on edit forms
      [laulaz]

- imio.smartweb.common 1.0.3

    - Hide faceted actions
      [boulch]

- imio.smartweb.common 1.0.2

    - Hide unwanted upgrades from site-creation and quickinstaller
      [boulch]

    - Add local manager role and sharing permissions rolemap
      [boulch]

    - Add help text on lead image fields
      [boulch]

    - Fix privacy views JS calls (sometimes called on Zope root instead of Plone root)
      [laulaz]

    - Add Subject keywords to SearchableText index
      [laulaz]

- Use released version for collective.z3cform.select2
  [laulaz]


1.0.3 (2022-03-29)
------------------

- Remove gunicorn timeout to allow long requests
  [laulaz]

- Switch collective.solr from auto-checkout to 9.0.0a6 pinned buildout.smartweb version
  [boulch]


1.0.2 (2022-03-16)
------------------

- imio.smartweb.common 1.0.1

    - Allow readers, editors and reviewers to see inactive (expired) contents
      [laulaz]

- imio.smartweb.common 1.0.

    - Avoid traceback if @@get_analytics is called outside Plone site
      [laulaz]

- imio.smartweb.common 1.0a11

    - Load Analytics via JS call to avoid non-privacy aware caching
      [laulaz]

    - Change privacy views permissions to zope.Public
      [laulaz]

- imio.smartweb.common 1.0a10

    - Hide ical import related actions
      [laulaz]

- imio.smartweb.common 1.0a9

    - Update buildout to use Plone 6.0.0a3 packages versions
      [boulch]

    - Remove unneeded override: it has been included in plone.app.z3c.form
      See https://github.com/plone/plone.app.z3cform/issues/138
      [laulaz]

- Use https:// instead of git:// protocol
  See https://github.blog/2021-09-01-improving-git-protocol-security-github/
  [boulch]


1.0.1 (2022-03-11)
------------------

- Use collective.taxonomy checkout to fix taxonomy data TTW edition
  [laulaz]


1.0 (2022-03-01)
----------------

- Use Gunicorn instead of Waitress.
  [bsuttor]

- Add py-spy for debugging.
  [bsuttor]


1.0a2-quick (2022-02-11)
------------------------

- imio.directory.core 1.0a2

    - Add more checks / automatic corrections in contacts CSV import
      [laulaz]

    - Update buildout to use Plone 6.0.0a3 packages versions
      [boulch]

- Update buildout to use Plone 6.0.0a3 packages versions
  [boulch]


1.0a1 (2022-01-26)
------------------

- Initial release
  [boulch]
