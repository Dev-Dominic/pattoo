#!/usr/bin/env/python3
"""Test pattoo installation shared script"""

from tests.libraries.configuration import UnittestConfig
import os
import getpass
import unittest
import sys
import tempfile
import yaml


# Try to create a working PYTHONPATH
EXEC_DIR = os.path.dirname(os.path.realpath(__file__))
ROOT_DIR = os.path.abspath(os.path.join(
    os.path.abspath(os.path.join(EXEC_DIR, os.pardir)), os.pardir))
_EXPECTED = '{0}pattoo{0}tests{0}test_setup'.format(os.sep)
if EXEC_DIR.endswith(_EXPECTED) is True:
    # We need to prepend the path in case the repo has been installed
    # elsewhere on the system using PIP. This could corrupt expected results
    sys.path.insert(0, ROOT_DIR)
    sys.path.append(os.path.join(ROOT_DIR, 'setup'))
else:
    print('''This script is not installed in the "{0}" directory. Please fix.\
'''.format(_EXPECTED))
    sys.exit(2)

from setup._pattoo.shared import _log, _run_script


class Test_Shared(unittest.TestCase):
    """Checks all functions for the Pattoo config script."""

    def test_log(self):
        """Unittest to test the _log function."""
        with self.assertRaises(SystemExit) as cm:
            _log("Test Error Message")
        self.assertEqual(cm.exception.code, 3)

    def test_run_script(self):
        """Unittest to test the _run_script function."""
        # Test case where the script should fail and exit with 2
        with self.subTest():
            with self.assertRaises(SystemExit) as cm:
                _run_script("this will exit with 2")
            self.assertEqual(cm.exception.code, 2)
        # Test case where the script should print "this works" to the console
        with self.subTest():
            expected = 0
            result = _run_script("echo this works")[0]
            self.assertEqual(result, expected)


if __name__ == '__main__':
    # Make sure the environment is OK to run unittests
    UnittestConfig().create()

    # Do the unit test
    unittest.main()
