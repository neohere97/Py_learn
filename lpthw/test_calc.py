import unittest
import calc

class test_calc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calc.add(10,6),16)
        self.assertEqual(calc.add(-5,6),1)
        self.assertEqual(calc.add(10.8,-0.8),10)
        self.assertEqual(calc.add(-20,"a"),"DTNS")
    def test_pow(self):
        self.assertEqual(calc.pow(2,3),8)
        self.assertEqual(calc.pow(2.2,3),2.2**3)
        self.assertEqual(calc.pow(2,-3),2**-3)
        self.assertEqual(calc.pow(2,"d"),"DTNS")
        
    def test_mod(self): 
        self.assertEqual(calc.mod(20,6),2)
        self.assertEqual(calc.mod(20,5),0)
        self.assertEqual(calc.mod(2,6),2)
        self.assertEqual(calc.mod(20,"d"),"DTNS")

if __name__ == '__main__':
    unittest.main()