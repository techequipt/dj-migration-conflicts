=============================
Django Detect Migration Conflict
=============================

.. image:: https://badge.fury.io/py/dj-migration-conflicts.svg
    :target: https://badge.fury.io/py/dj-migration-conflicts

.. image:: https://travis-ci.org/techequipt/dj-migration-conflicts.svg?branch=master
    :target: https://travis-ci.org/techequipt/dj-migration-conflicts

.. image:: https://codecov.io/gh/techequipt/dj-migration-conflicts/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/techequipt/dj-migration-conflicts

Management command to detect migration conflicts and raise an error if found

Quickstart
----------

Install Django Detect Migration Conflict::

    pip install dj-migration-conflicts

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'dj_migration_conflicts.apps.DjMigrationConflictsConfig',
        ...
    )


Features
--------

- Migration command to check for migration conflicts. To run it run:
`python manage.py detect_migration_conflicts`

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox


Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage

Attribution: library is based on this gist: https://gist.github.com/cb109/9f434e83c86e122715b78766e1dde2da
