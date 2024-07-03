import fractions 

def sumNumbers(a = 5, b = 5): 
   sums = [] 
   sumOfNumbers_1 = a + b 
   sumOfNumbers_2 = sumOfNumbers_1 + a + b 
   sumOfNumbers_3 = sumOfNumbers_2 + sumOfNumbers_1 + a + b 
   sums.append(sumOfNumbers_1) 
   sums.append(sumOfNumbers_2) 
   sums.append(sumOfNumbers_3) 
   return sums 

def sumFractions(a = fractions.Fraction(1, 2), b = fractions.Fraction(1, 4)): 
   sums = [] 
   sumOfFractions1 = a + b 
   sumOfFractions2 = sumOfFractions1 + a + b 
   sumOfFractions3 = sumOfFractions1 + sumOfFractions2 + a + b 
   sums.append(sumOfFractions1) 
   sums.append(sumOfFractions2) 
   sums.append(sumOfFractions3) 
   return sums 