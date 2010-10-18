======
susola
======

Different useful scripts for use on openSUSE_ Linux or other Linux
distributions.

Installation
============

First, you need to build fresh RPM package and then to install it. For
simplification, I recomend execute next commands for this::

    $ make
    # make install

If you already have ``susola`` installed to your system ``Makefile`` auto
update it with fresh version.

To uninstall, just remove ``susola`` package with ``rpm -e`` command::

    # rpm -e susola

License
=======

``susola`` is licensed under the `BSD License
<http://github.com/playpauseandstop/susola/blob/master/LICENSE>`_.

Contents
========

sysinfo2web
-----------

Very tiny web page generated in real-time with basic sysinfo about Linux
system.

Requirements
~~~~~~~~~~~~

* Python_ 2.4 or higher

Usage
~~~~~

This script is small and efficient for me replacement of sysinfo2html_,
phpSysInfo_ or ajenti_.

To enable ``sysinfo2web``, just execute::

    $ sysinfo2web

And point your browser to ``http://127.0.0.1:8000/`` to see results.

To customize ip or port on which ``sysinfo2web`` script would be ran setup
this values manually, like::

    $ sysinfo2web <ip>:<port>

or::

    $ sysinfo2web :<port>

After changing ip or port, point browser to new URI to see system information
about your Linux machine.

.. _sysinfo2html: http://www.mrleejohn.nl/sysinfo2html/
.. _phpSysInfo: http://phpsysinfo.sourceforge.net/
.. _ajenti: http://github.com/Eugeny/ajenti

zypper-bin
----------

**B**atch **in**stall all packages earlier found by ``zypper se -u``.

Requirements
~~~~~~~~~~~~

* zypper_
* Python_ 2.4 or higher

Usage
~~~~~

If sometimes, you need to install all packages found by ``zypper se -u``
command in batch mode - use ``zypper-bin`` script::

    # zypper se -u <package> | zypper-bin

zypper-brm
----------

**B**atch **r**e**m**ove all packages earlier found by ``zypper se -i``.

Requirements
~~~~~~~~~~~~

* zypper_
* Python_ 2.4 or higher

Usage
~~~~~

By default, openSUSE shipped with ``*-{de|fr|it|pl|ru}`` locale packages that
in most cases unneeded. Then you can to found all of these packages, but
cannot remove. To avoid this - use ``zypper-brm`` script::

    # zypper se -i "*-de" | zypper-brm

Also, you can use script after show all installed packages in some repo and
grepping data::

    # zypper pa -i <repo> | grep <package> | zypper-brm pa

zypper-iuc
----------

**I**nstall **u**pdate **c**andidates from different repositories.

Requirements
~~~~~~~~~~~~

* zypper_
* Python_ 2.4 or higher

Usage
~~~~~

Sometimes, you can have un-installable packages when running ``# zypper up``
command. In general case this means that packages are from different repository
and you need to install it directly with ``$ zypper in <package>-<version>``.

To automate this process - use ``zypper-iuc`` script::

    # zypper up <package> | zypper-iuc

zypper-mrum
-----------

Script to enable (**m**odify) repo, **r**efresh, **u**pdate all packages from
it and disable (**m**odify) repo.

Requirements
~~~~~~~~~~~~

* zypper_

Usage
~~~~~

This script created to add ability update packages from Packman_ repository one
time per week, but update other packages any times per week.

::

    # zypper-mrum <repo>

equals to::

    # zypper mr -e <repo> && \
    zypper ref <repo> && \
    zypper up -r <repo> && \
    zypper mr -d <repo>

zypper-ur
---------

**U**pdate urls for all zypper **r**epositories to new openSUSE version.

Requirements
~~~~~~~~~~~

* zypper_
* Python_ 2.4 or higher

Usage
~~~~~

This script is useful if you want to upgrade your openSUSE installation from
some version to next and also want to keep all of your repositories.

::

    # zypper-ur <version>

where ``<version>`` is valid openSUSE version, like ``11.2`` or ``11.3``.

.. _openSUSE: http://www.opensuse.org/
.. _zypper: http://en.opensuse.org/Portal:Zypper
.. _Packman: http://packman.links2linux.org/
.. _Python: http://www.python.org/
