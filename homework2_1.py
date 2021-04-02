class Fraction:

     def __init__(self,a,b):
         self.num = a
         self.den = b


     def __str__(self):
         return str(self.num)+"/"+str(self.den)

     def show(self):
         print(str(self.num)+"/"+str(self.den))

     # def __add__(self, num1, den1):
     #     self.num1 = num1
     #     self.den1 = den1

f = Fraction(2, 8)
print(f)




# def __add__(self, num, den, num1, den1):
#     self.a = num
#     self.b = den
#     self.c = num1
#     self.d = den1
#     x = f'(a * d + b * c)
#     y = f'(b * d)
#
#     print(x, '/', y)


