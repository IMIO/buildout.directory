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
