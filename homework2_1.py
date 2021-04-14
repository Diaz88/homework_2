class Fraction:

     def __init__(self,num,den):
         if den == 0:
             raise ValueError("Denominator can't 0!")
         self.num = num
         self.den = den


     def add(self, other):
         num = self.num * other.den + other.num * self.den
         den = self.den * other.den
         print(num)
         print('-')
         print(den)


f = Fraction(2, 8)
f1 = Fraction(3 , 9)
f.add(f1)

