=====
Usage
=====

To use Django Detect Migration Conflict in a project, add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'dj_migration_conflicts.apps.DjMigrationConflictsConfig',
        ...
    )

Add Django Detect Migration Conflict's URL patterns:

.. code-block:: python

    from dj_migration_conflicts import urls as dj_migration_conflicts_urls


    urlpatterns = [
        ...
        url(r'^', include(dj_migration_conflicts_urls)),
        ...
    ]
