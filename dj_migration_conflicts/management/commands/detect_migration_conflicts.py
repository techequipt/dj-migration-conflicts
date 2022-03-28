# Attributed to https://gist.github.com/cb109/9f434e83c86e122715b78766e1dde2da

import re
from io import StringIO
from textwrap import dedent

from django.core.management import call_command
from django.core.management.base import BaseCommand, CommandError
from django.db import DEFAULT_DB_ALIAS, connections
from django.db.migrations.executor import MigrationExecutor


class Command(BaseCommand):
    help = "Check migrations for conflicts and descriptive filenames"

    def add_arguments(self, parser):
        parser.add_argument(
            "descriptive-names",
            dest="descriptive_names",
            action="store_true",
            help="Also check for descriptive migration names",
        )

    def handle(self, *args, **options):
        self._check_for_migration_conflicts()
        if options.get("descriptive_names"):
            self._check_pending_migrations_use_descriptive_filename()

    def _check_for_migration_conflicts(self):
        # Snippet below is copied straight from the Django source:
        # django/core/management/commands/migrate.py

        connection = connections[DEFAULT_DB_ALIAS]
        connection.prepare_database()

        executor = MigrationExecutor(connection, lambda *args, **kwargs: None)
        executor.loader.check_consistent_history(connection)

        conflicts = executor.loader.detect_conflicts()
        if conflicts:
            name_str = "; ".join(
                "%s in %s" % (", ".join(names), app)
                for app, names in list(conflicts.items())
            )
            raise CommandError(
                "Conflicting migrations detected; multiple leaf nodes in the "
                "migration graph: (%s).\nTo fix them run "
                "'python manage.py makemigrations --merge'" % name_str
            )

    def _check_pending_migrations_use_descriptive_filename(self):
        """Warn about 1234_auto_XYZ.py migration files (pending only)."""

        temp_stdout = StringIO()
        call_command("migrate", "--plan", "--no-color", stdout=temp_stdout)
        output_text = temp_stdout.getvalue()

        pattern = re.compile(r"(?P<app_label>\w+)\.(?P<auto_migration>\d{4}\_auto_\w+)")
        pending_auto_migrations = pattern.findall(output_text)

        warning_message = "Please rename the following migrations:\n\n"
        for app_label, migration_name in pending_auto_migrations:
            warning_message += f"  - {app_label}.{migration_name}\n"
        warning_message += dedent(
            """
            It is helpful to give migration files a meaningful name, so
            that scanning the migrations list allows us to identify
            related changes that may need extra care before/after
            migrating. This can be done on creation as well by:
                manage.py makemigrations --name mymodel_add_newfield
            Ideally the migration filename should mention the model(s)
            and/or field name(s) that are affected (changed, added,
            removed). Make sure to upgrade dependencies as well.
            """
        )
        raise CommandError(warning_message)
