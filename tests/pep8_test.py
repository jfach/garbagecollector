import os
import unittest
import pep8
import fixture

class TestPep8(fixture.TestFixture):
    """
    Run PEP8 tests.
    """
    def test_conformance(self):
        checker = pep8.StyleGuide(paths=[os.curdir], reporter=pep8.StandardReport)
        report = checker.check_files()
        result = report.total_errors
        output = "\n".join(report.get_statistics())
        if result != 0:
            self.fail("Found PEP8 errors:\n%s" % output)
