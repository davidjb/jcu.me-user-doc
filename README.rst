User documentation
==================

End-user documentation for the Research Portfolio.

Documentation is available at http://jcu-me.rtfd.org, produced after each
push to this repository.

About this documentation
------------------------

* Powered by Sphinx
* Configuration-based documentation: an example of using conditional statments
  to build up documentation.  Just look for ``ifconfig`` sections and the
  example config in ``source/conf.py``.
* Project-wide substitutions: set key aspects to the documentation like
  project name and URL in one location (``source/conf.py``) and use the
  ``|substitution|`` markup accordingly in any document.
* Branchable for different projects: just customise the screenshots and
  ``source/conf.py`` settings.

Install
-------

To install all dependencies and then build the actual documentation, do
the following::

    virtualenv . -p /usr/bin/python3
    source ./bin/activate
    python bootstrap-buildout.py
    ./bin/buildout
    ./bin/sphinxbuilder

To re-build the documentation, just run::

    ./bin/sphinxbuilder

The final path of the rendered documentation is described in the console
output.

Features
--------

* Flexible images for HTML and LaTeX (PDF) output (``.. image:: ``)
