================
 OpenSlides GUI
================

Overview
========

Simple GUI frontend for `OpenSlides <http://openslides.org/>`_ to run and configure OpenSlides' web server.
Used with `OpenSlides Portable <https://github.com/OpenSlides/openslides-portable>`_ to build a full portable distribution of OpenSlides.


Requirements
============

- Python 3.4+
- OpenSlides 2.x
- wxPython-Phoenix
- psutil

See requirements.txt


Install
=======

This is an instruction to install OpenSlides GUI.

1. Install Python 3.4+ and Setuptools

   Follow the instructions in the README of OpenSlides.


2. Install wxPython_Phoenix

   Install wheel (whl) file from the official (unfortunately untrusted http)
   `snapshot url <http://wxpython.org/Phoenix/snapshot-builds>`_.
   For easier installation we have to wait once wxPython-Phoenix is released on pypi.python.org.

   Example install command for Python 3.4 on Windows (32bit)::

    $ pip install -f --trusted-host http://wxpython.org/Phoenix/snapshot-builds/wxPython_Phoenix-3.0.3.dev1964+f780b21-cp34-cp34m-win32.whl


3. Install OpenSlides 2.x package with all requirements::

   $ pip install openslides-2.x


4. Install openslides-gui::

   $ pip install openslides-gui


5. Run the OpenSlides GUI::

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
