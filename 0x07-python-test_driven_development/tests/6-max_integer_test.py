import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Unitests created for the module 6-max_integer"""

    def test_module_docstring(self):
        """Test if module docstring is prensent"""
        m_documentation = __import__('6-max_integer').__doc__
        self.assertTrue(len(m_documentation) > 1)

    def test_function_docstring(self):
        """Test if function docstring is prensent"""
        f_documentation = __import__('6-max_integer').max_integer.__doc__
        self.assertTrue(len(f_documentation) > 1)

    def test_other_sequences(self):
        with self.assertRaises(TypeError):
            max_integer([None, True])
        with self.assertRaises(TypeError):
            max_integer([-10, 0.5, "str", {1, 2}])
        with self.assertRaises(TypeError):
            max_integer({1, 2, 3, 4, 5})
        with self.assertRaises(TypeError):
            max_integer({1, 2}, {3, 4, 5})

    def test_signed_ints_and_floats(self):
        """Test for equality"""
        self.assertEqual(max_integer([0]), 0)
        self.assertEqual(max_integer([1, 2, 3, -4]), 3)
        self.assertEqual(max_integer([-1.5, -2.5]), -1.5)
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_lists(self):
        """Test for equality in lists"""
        self.assertEqual(max_integer([[1, 2], [1, 3]]), [1, 3])

    def test_list_of_strings(self):
        """Test for sequences of charactes in lists"""
        self.assertEqual(max_integer(['a', 'b', 'c', 'x', 'y', 'z']), 'z')
        self.assertEqual(max_integer("6789"), '9')
        self.assertEqual(max_integer(["abc", 'x']), 'x')
        self.assertEqual(max_integer("abcxyz"), 'z')

    def test_None(self):
        """Test for None availability"""
        self.assertIsNone(max_integer([]), None)
        self.assertIsNone(max_integer(), None)

if __name__ == "__main__":
    unittest.main()
