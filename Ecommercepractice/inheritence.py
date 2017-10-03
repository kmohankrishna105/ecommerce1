"""
from Ecommercepractice.Classmethods import sequence
import unittest

class terminate(sequence,unittest.TestCase):
    #@classmethod
    def Test_name(self):
        print("shi")

if __name__=="__main__":
    unittest.main()

#
g=terminate()
g.Test_name()
"""


class parent:
    def __init__(self):
        print ("This is a parent")

    def fucn(self):
        print ("Not a overridden function")

