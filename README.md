# XL Release Delphix plugin

[![Build Status][xlr-delphix-plugin-travis-image]][xlr-delphix-plugin-travis-url]
[![License: MIT][xlr-delphix-plugin-license-image]][xlr-delphix-plugin-license-url]
![Github All Releases][xlr-delphix-plugin-downloads-image]
[![FOSSA Status](https://app.fossa.io/api/projects/git%2Bgithub.com%2Fxebialabs-community%2Fxlr-delphix-plugin.svg?type=shield)](https://app.fossa.io/projects/git%2Bgithub.com%2Fxebialabs-community%2Fxlr-delphix-plugin?ref=badge_shield)

[xlr-delphix-plugin-travis-image]: https://travis-ci.org/xebialabs-community/xlr-delphix-plugin.svg?branch=master
[xlr-delphix-plugin-travis-url]: https://travis-ci.org/xebialabs-community/xlr-delphix-plugin
[xlr-delphix-plugin-license-image]: https://img.shields.io/badge/License-MIT-yellow.svg
[xlr-delphix-plugin-license-url]: https://opensource.org/licenses/MIT
[xlr-delphix-plugin-downloads-image]: https://img.shields.io/github/downloads/xebialabs-community/xlr-delphix-plugin/total.svg

![Google Compute](src/main/resources/delphix/delphix.png)

## Preface

This document describes the functionality provided by the XLRelease plugin for Delphix.

See the [XL Release reference manual](https://docs.xebialabs.com/xl-release) for background information on XL Release and release automation concepts.  

## Overview

## Requirements

You need to have Jython installed to run unit tests.

Note: XLR version should not be lower than lowest supported version.  See <https://support.xebialabs.com/hc/en-us/articles/115003299946-Supported-XebiaLabs-product-versions>.
The plugins uses the REST API (1.10.0) exposed by the server.


## Installation

* Copy the latest JAR file from the [releases page](https://github.com/xebialabs-community/xlr-delphix-plugin/releases) into the `XL_RELEASE_SERVER/plugins/__local__` directory.
* Restart the XL Release server.

## Features/Usage/Types/Tasks

The tasks are:
* Refresh
* Rewind
* Snapshot
* Start
* Stop
* Delete
* Disable
* Enable

## References

* https://docs.delphix.com/docs/reference/web-service-api-guide/web-service-protocol
* https://docs.delphix.com/docs/reference/web-service-api-guide/web-service-object-model
* https://docs.delphix.com/docs/reference/web-service-api-guide/api-cookbook-common-tasks-workflows-and-examples/api-cookbook-stop-start-a-vdb

# TODO
* Move to the python SDK
* Add job action output on every task script




## License
[![FOSSA Status](https://app.fossa.io/api/projects/git%2Bgithub.com%2Fxebialabs-community%2Fxlr-delphix-plugin.svg?type=large)](https://app.fossa.io/projects/git%2Bgithub.com%2Fxebialabs-community%2Fxlr-delphix-plugin?ref=badge_large)