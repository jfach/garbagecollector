import pep8
from fixture import TestFixture, REPO_DIR


class TestPep8(TestFixture):
    """
    Run PEP8 tests.
    """
    def test_conformance(self):
        checker = pep8.StyleGuide(paths=[REPO_DIR], reporter=pep8.StandardReport)
        report = checker.check_files()
        result = report.total_errors
        output = "\n".join(report.get_statistics())
        if result != 0:
            self.fail("Found PEP8 errors:\n%s" % output)
