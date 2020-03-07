import unittest

import calc2

class TestAdd(unittest.TestCase):
    """
    Test add method of Calc class
    """

    def test_add_integers(self):
        """
        Test that the addition of two integers returns the correct result
        """

        result = calc2.Calc().add(1,2)
        self.assertEqual(result, 3)

    def test_add_floats(self):
        """
        Test that the addition of two floats returns the correct result
        """

        result = calc2.Calc().add(10.5, 2)
        self.assertAlmostEqual(result, 12.5, 5)

    def test_add_string(self):
        """
        Test the addition of two strings returns one concatenated string
        """
        result = calc2.Calc().add('abc', 'def')
        self.assertEqual(result, 'abcdef')


class TestMultiple(unittest.TestCase):
    def test_multiple_integers(self):
        self.assertEqual(calc2.Calc().multiple(10, 5), 50)
        self.assertEqual(calc2.Calc().multiple(-1, 1), -1)
        self.assertEqual(calc2.Calc().multiple(-1, -1), 1)

if __name__ == "__main__":
    unittest.main()