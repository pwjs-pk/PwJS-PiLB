from math import sqrt


class ComplexNumber:

    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return ComplexNumber(self.real - other.real, self.imag - other.imag)

    def __abs__(self):
        return sqrt(self.real ** 2 + self.imag ** 2)

    def __mul__(self, other):
        return ComplexNumber(self.real * other.real - self.imag * other.imag,
                             self.imag * other.real + self.real * other.imag)

    def __str__(self):
        return f"{self.real}{'+' + str(self.imag) if self.imag >= 0  else str(self.imag)}i"


if __name__ == '__main__':
    c1 = ComplexNumber(-22, 33)
    c2 = ComplexNumber(21, -24)
    print(f" ({c1}) - ({c2}) = {c1 - c2}")
    print(f" ({c1}) + ({c2}) = {c1 + c2}")
    print(f" ({c1}) * ({c2}) = {c1 * c2}")
    print(f"|{c2}| = {abs(c2)}")
