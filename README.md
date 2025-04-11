# buildout.directory

This repository contains the Buildout configuration for **Directory**, the centralized contact directory platform used by Walloon local authorities (pouvoirs locaux). It is part of the broader Smartweb ecosystem and integrates seamlessly with Plone 6-based Smartweb sites.

## Overview

The **Directory** platform provides a shared environment where multiple local authorities can create, manage, and publish contact information (services, persons, roles, etc.). These directories can then be synchronized and displayed on Smartweb websites.

This `buildout.directory` repository contains the complete Buildout setup to install, configure, and deploy the centralized Plone 6 instance used to manage contact directories.

## Purpose

- Provide a central point of truth for contact data.
- Allow reuse and synchronization of contact information across multiple local authority sites.
- Enable integration with Smartweb via Solr or REST APIs.

## Integration with Smartweb

Smartweb websites fetch directory data from this centralized instance, enabling:

- Cross-site display of up-to-date contact information
- Centralized management of persons, organizations, and services
- Better performance and consistency through external Solr indexing or REST API usage

## Contributing

Feel free to open issues or submit pull requests if you find bugs or want to improve the setup.

## Maintainers

- iMio
