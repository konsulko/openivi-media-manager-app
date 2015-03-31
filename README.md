# Media Manager

## Introduction
---
Media Manager is an AGL Open Source HTML5 proof-of-concept application. It's purpose is to provide a user interface for the GENIVI Media Manager project. You can find that project at GENIVI (http://wiki.projects.genivi.org/index.php/Media_Manager)

## Maintainers
---
The primary maintainer of the project is Aaron Eiche
He can be contacted at aeiche@jaguarlandrover.com

## Dependencies
---
To run the software, the project requires the following:
* A platform running the most recent AGL release
* Installed GENIVI Media Manager
* The built widget, installed on the platform.

## Getting Started
---
Built releases of Media Manager are available at the [Automotive Grade Linux site](https://www.automotivelinux.org/software/). It is recommended if you simply want to interact with the software that you get the most recent stable release from AGL. Further instructions are provided below for building and deploying from source.

## Building
---
#### Building Widgets
Make files are provided in repositories to package widgets for installation on AGL. 

To build and copy the wgt files to the platform: `make deploy`  
To build and install widgits on the platform: `make install.feb1`  
To build, install and run on the platform: `make run.feb1`

## Contributing
------------
If you would like to contribute to the project, please fork into your github account. Develop your code changes, test and commit. Issue a pull request to the PDXostc/media_manager-app. The pull request will go through the review process at GerritHub and merged, or rejected if necessary.