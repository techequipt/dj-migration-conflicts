#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_dj-migration-conflicts
------------

Tests for `dj-migration-conflicts` models module.
"""

import logging

from django.conf import settings
from django.core.management import call_command
from django.core.management.base import CommandError

logger = logging.getLogger(__name__)


def test_no_conflicting_migration_by_multiple_leaf_nodes_in_graph(db, monkeypatch):
    """Raise a CommandError in case of conflicts.
    This test merely exists to catch migration conflicts even when
    tests are run with --no-migrations or migrations are skipped/
    disabled by some other mechanism.
    """

    # Revert the --no-migrations effect to ensure migrations are run.
    monkeypatch.setattr(settings, "MIGRATION_MODULES", {})

    try:
        call_command("checkmigrations")
    except CommandError as err:
        logger.exception(err)
        raise
