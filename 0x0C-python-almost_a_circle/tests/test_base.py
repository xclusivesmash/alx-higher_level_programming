#!/usr/bin/python3
"""Module: test_base"""
import unittest
import pep8
from models.base import Base


class TestPEP8(unittest.TestCase):
    """PEP8 COMPLIANCE"""
    def test_PEP8(self):
        error_count = 0
        style = pep8.StyleGuide()
        files = ["models/base.py", "tests/test_base.py"]
        error_count = error_count + style.check_files(files).total_errors
        self.assertEqual(error_count, 0, "PEP8 not compliant")
        return None


class TestBase(unittest.TestCase):
    """Test cases for Base class."""
    def test_id_passed(self):
        """Test for Id values given."""
        self.assertTrue(Base(1), self.id == 1)
        self.assertTrue(Base(16), self.id == 16)
        return None

    def test_id_not_passed(self):
        """Id values not passed."""
        self.assertTrue(Base(), self.id == 1)
        self.assertTrue(Base(), self.id == 2)
        self.assertTrue(Base(), self.id == 3)
        return None

# INCOMPLETE: NEED TO COMPLETE MORE TESTS TO COME


if __name__ == "__main__":
    unittest.main()
