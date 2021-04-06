class Complex:

    def __init__(self, re, im):
        self.re = re
        self.im = im

    def __add__(self, other):

        a = self.re + other.re
        b = self.im + other.im
        Complex(a, b)
        return a + b
        
        # a = self.re - other.re
        # b = self.im - other.im
        # Complex(a, b)
        # return a + b

        # a = self.re + self.im
        # b = other.re + other.im
        # Complex(a, b)
        # return a * b


        # a = self.re + self.im
        # b = other.re + other.im
        # print(a)
        # print('-')
        # Complex(a, b)
        # return b


complex1 = Complex(10, 5j)
complex2 = Complex(22, 8j)
complex3 = complex1 + complex2
print(complex3)



