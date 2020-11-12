import unittest
import pacman

class TestCase1(unittest.TestCase):

    # Change the FILE in pacman.py and run individual test
    def test_case1(self):
        self.assertEqual(pacman.report(), 'Output: 0,1,NORTH')

    # def test_case2(self):
    #     self.assertEqual(pacman.report(), 'Output: 0,0,WEST')

    # def test_case3(self):
    #     self.assertEqual(pacman.report(), 'Output: 3,3,NORTH')

    # def test_case4(self):
    #     self.assertEqual(pacman.report(), 'Output: 0,4,NORTH')

    # def test_case5(self):
    #     self.assertEqual(pacman.report(), 'Output: 4,0,EAST')

    # def test_case6(self):
    #     self.assertEqual(pacman.report(), 'Output: 0,0,WEST')

# TESTING OUTPUT
# IE aylwin$ python3 -m unittest test_pacman.py 
# Output: 0,1,NORTH
# Output: 0,1,NORTH
# .Output: 0,1,NORTH
# IE aylwin$ python3 -m unittest test_pacman.py 
# Output: 0,1,NORTH
# Output: 0,1,NORTH
# .
# ----------------------------------------------------------------------
# Ran 1 test in 0.001s

# OK
# IE aylwin$ python3 -m unittest test_pacman.py 
# Output: 0,0,WEST
# Output: 0,0,WEST
# .
# ----------------------------------------------------------------------
# Ran 1 test in 0.007s

# OK
# IE aylwin$ python3 -m unittest test_pacman.py 
# Output: 3,3,NORTH
# Output: 3,3,NORTH
# .
# ----------------------------------------------------------------------
# Ran 1 test in 0.001s

# OK
# IE aylwin$ python3 -m unittest test_pacman.py 
# Output: 0,4,NORTH
# Output: 0,4,NORTH
# .
# ----------------------------------------------------------------------
# Ran 1 test in 0.001s

# OK
# IE aylwin$ python3 -m unittest test_pacman.py 
# Output: 4,0,EAST
# Output: 4,0,EAST
# .
# ----------------------------------------------------------------------
# Ran 1 test in 0.007s

# OK
# IE aylwin$ python3 -m unittest test_pacman.py 
# Output: 0,0,WEST
# Output: 0,0,WEST
# .
# ----------------------------------------------------------------------
# Ran 1 test in 0.000s

# OK



        
    