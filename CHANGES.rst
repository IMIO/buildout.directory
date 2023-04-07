1.2.6 (unreleased)
------------------

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
