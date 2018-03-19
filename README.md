# XL Release Delphix plugin v1.0.0

[![Build Status][xlr-delphix-plugin-travis-image]][xlr-delphix-plugin-travis-url]
[![License: MIT][xlr-delphix-plugin-license-image]][xlr-delphix-plugin-license-url]
![Github All Releases][xlr-delphix-plugin-downloads-image]

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

Note: XLR version should not be lower than lowest supported version.  See <https://support.xebialabs.com/hc/en-us/articles/115003299946-Supported-XebiaLabs-product-versions>.
The plugins uses the REST API (1.8.2) exposed by the server.


## Installation

* Copy the latest JAR file from the [releases page](https://github.com/xebialabs-community/xlr-delphix-plugin/releases) into the `XL_RELEASE_SERVER/plugins` directory.
* Restart the XL Deploy|Release server.

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


