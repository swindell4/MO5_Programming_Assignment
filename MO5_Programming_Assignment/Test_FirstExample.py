import unittest
import FirstExample 
import fractions
class TestSum(unittest.TestCase):
  
   def test_list_int(self):
      self.result = FirstExample.sumNumbers() 
      self.result = sum(self.result) 
      self.assertEqual(self.result, 70) 

#I used a list of integers 10 20 and 40. sice the test passed I can assume that 10 + 20 + 40 == 70. 

   def test_list_fractions(self): 
      self.result = FirstExample.sumFractions() 
      self.result = sum(self.result) 
      self.assertEqual(self.result, fractions.Fraction(21, 4)) 

#I used a list of fractions 3/4, 3/2, and 3/1. I tested it agains int(3) and it failed. This is because the sum of the fractions was 21/4. 

if __name__ == '__main__': 
    unittest.main() 