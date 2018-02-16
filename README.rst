================
 OpenSlides GUI
================

Overview
========

Simple GUI frontend for `OpenSlides <http://openslides.org/>`_ to run and configure OpenSlides' web server.
Used with `OpenSlides Portable <https://github.com/OpenSlides/openslides-portable>`_ to build a full portable distribution of OpenSlides.


Requirements
============

- Python 3.5+
- OpenSlides 2.2
- wxPython 4.x (Phoenix)

See requirements.txt


Install
=======

This is an instruction to install OpenSlides GUI.

1. Install Python 3.5+ and Setuptools

   Follow the instructions in the README of OpenSlides.


2. Install requirements::

   $ pip install -r requirements.txt


3. Install openslides-gui::

   $ pip install openslides-gui


4. Run the OpenSlides GUI::

   $ openslides-gui


License
=======

This plugin is Free/Libre Open Source Software and distributed under the
MIT License, see LICENSE file.


Authors
=======

* Andy Kittner <andkit@gmx.net>
* Emanuel Schütze <emanuel@intevation.de>


Changelog
=========

Version 1.1.4 (2018-02-16)
--------------------------
* Use get_default_user_data_dir instead of get_default_user_data_path
* Updated wxphoenix.
* Updated credits.

Version 1.1.3 (2017-11-17)
--------------------------
* Install wxpython from pypi.

Version 1.1.2 (2017-03-29)
--------------------------
* Don't kill browser after stopping server.
  (Removed psutil as requirements)
* Added option to use Geiss and Redis server.

Version 1.1.1 (2017-01-26)
--------------------------
* Updated README to Python 3.5.
* Updated Credits to 2016.

Version 1.1 (2016-03-21)
------------------------
* Added port/host arguments for openslides start command.
* Improved OpenSlides app icon.

Version 1.0.1 (2016-02-03)
--------------------------
* Updated README to Python 3.4.
* Updated Credits to 2016.

Version 1.0 (2015-12-07)
------------------------
* First release of openslides-gui for OpenSlides 2.x.
  It's moved from old OpenSlides 1.x repository into an own openslides-gui package.
