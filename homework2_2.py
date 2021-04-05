

class Complex:

    def __init__(self, re, im):
        self.re = re
        self.im = im

    def __add__(self, other):

        a = self.re + other.re
        b = self.im + other.im
        return f'{a} + {b} i'

        # a = self.re - other.re
        # b = self.im - other.im
        # return f'{a} + {b} i'

        # a = self.re + self.im
        # b = other.re + other.im
        # return a * b


        # a = self.re + self.im
        # b = other.re + other.im
        # print(a)
        # print('-')
        # return b


complex1 = Complex(10, 5)
complex2 = Complex(22, 8)
complex3 = complex1 + complex2
print(complex3)


