import os
import pep8


def test():
    """
    Run PEP8 tests.
    """
    checker = pep8.StyleGuide(paths=[os.curdir], reporter=pep8.StandardReport)
    report = checker.check_files()
    result = report.total_errors
    output = "\n".join(report.get_statistics())
    if result != 0:
        raise Exception("\n"+output)
    else:
        pass    
