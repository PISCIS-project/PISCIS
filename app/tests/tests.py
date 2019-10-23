# This file is part of the:
#   Piscis Project (https://github.com/mkoraj/piscis).
# Copyright (c) 2019-2020, PISCIS
# License: BSD-3-Clause
#   Full Text: https://github.com/mkoraj/piscis/blob/master/LICENSE

from django.test import TransactionTestCase
from django.test.runner import DiscoverRunner
from unittest.suite import TestSuite

class UnitTestRunner(DiscoverRunner):
    def setup_databases(self, **kwargs):
        pass
    def teardown_databases(self, old_config, **kwargs):
        pass
    def build_suite(self, **kwargs):
        suite = super().build_suite(**kwargs)
        tests = [t for t in suite._tests if self.is_unittest(t)]
        return TestSuite(tests=tests)
    def is_unittest(self, test):
        return not issubclass(test.__class__, TransactionTestCase)

