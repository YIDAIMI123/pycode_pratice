import unittest
from pycode_pratice.add import add

class my_test(unittest.TestCase):

    def test_add(self): #因为只有一个测试用例，所以只测试一次
        self.assertEqual(add(1,2),3)
        self.assertEqual(add(-1,1),0)
        self.assertEqual(add(0,0),0)
        self.assertEqual(add(-1,-1),-2)
        self.assertEqual(add(1.5,2.5),4.0)
        self.assertEqual(add(-1.5,1.5),0.0)