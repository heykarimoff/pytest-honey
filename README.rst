============
pytest-honey
============

.. image:: https://img.shields.io/pypi/v/pytest-honey.svg
    :target: https://pypi.org/project/pytest-honey
    :alt: PyPI version

.. image:: https://img.shields.io/pypi/pyversions/pytest-honey.svg
    :target: https://pypi.org/project/pytest-honey
    :alt: Python versions

.. image:: https://ci.appveyor.com/api/projects/status/github/heykarimoff/pytest-honey?branch=master
    :target: https://ci.appveyor.com/project/heykarimoff/pytest-honey/branch/master
    :alt: See Build Status on AppVeyor

A simple plugin to use with pytest

----

This `pytest`_ plugin was generated with `Cookiecutter`_ along with `@hackebrot`_'s `cookiecutter-pytest-plugin`_ template.


Features
--------

- Adds ``--honey`` option that:
    - turns ``F`` to ``HONEY``
    - with ``-v``, turns ``FAILURE`` to ``HONEY for bread.``


Requirements
------------

- pytest >=3.5.0


Installation
------------

You can install "pytest-honey" via `pip`_ from `PyPI`_::

    $ pip install pytest-honey


Usage
-----

::
    $ pytest --honey


Contributing
------------
Contributions are very welcome. Tests can be run with `tox`_, please ensure
the coverage at least stays the same before you submit a pull request.

License
-------

Distributed under the terms of the `MIT`_ license, "pytest-honey" is free and open source software


Issues
------

If you encounter any problems, please `file an issue`_ along with a detailed description.

.. _`Cookiecutter`: https://github.com/audreyr/cookiecutter
.. _`@hackebrot`: https://github.com/hackebrot
.. _`MIT`: http://opensource.org/licenses/MIT
.. _`BSD-3`: http://opensource.org/licenses/BSD-3-Clause
.. _`GNU GPL v3.0`: http://www.gnu.org/licenses/gpl-3.0.txt
.. _`Apache Software License 2.0`: http://www.apache.org/licenses/LICENSE-2.0
.. _`cookiecutter-pytest-plugin`: https://github.com/pytest-dev/cookiecutter-pytest-plugin
.. _`file an issue`: https://github.com/heykarimoff/pytest-honey/issues
.. _`pytest`: https://github.com/pytest-dev/pytest
.. _`tox`: https://tox.readthedocs.io/en/latest/
.. _`pip`: https://pypi.org/project/pip/
.. _`PyPI`: https://pypi.org/project
