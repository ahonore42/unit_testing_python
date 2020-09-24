import unittest
# PYTHON modue for unit testing
import calc

# create a test class
# test is a key word in unittest
class TestCalc(unittest.TestCase):

    def test_add(self):
        result = calc.add(10, 5)
        self.assertEqual(result, 15)
        # shoud return 15
        self.assertEqual(calc.add(100, 1), 101)
        # shoud return 101
        self.assertEqual(calc.add(-88, 88), 0)
        # shoud return 0
        self.assertEqual(calc.add(2, 2), 4)
        # shoud return 0
        # pass in the result we get as a return
        # and the correct result we're looking for



if __name__ == '__main__':
    unittest.main()
# this will run every possible unit test in the file
# to run this file with this method, simply enter 'python3 test_calc.py'


# to run this file without any function calls written like the one above, run
# python3 -m unittest test_calc.py

# A success return will look like this
# .
# ----------------------------------------------------------------------
# Ran 1 test in 0.000s

# OK

# A failure will look like this
# F
# ======================================================================
# FAIL: test_add (test_calc.TestCalc)
# ----------------------------------------------------------------------
# Traceback (most recent call last):
#   File "/Users/adamhonore/sei30/unit4/code-alongs/unit_testing_python/test_calc.py", line 12, in test_add
#     self.assertEqual(result, 14)
# AssertionError: 15 != 14

# ----------------------------------------------------------------------
# Ran 1 test in 0.000s

# FAILED (failures=1)