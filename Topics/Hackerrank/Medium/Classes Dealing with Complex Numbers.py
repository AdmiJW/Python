

#   First, the Complex class inherits the object class (Although without it is still perfectly fine)
#
#   __add__, __sub__, __mul__, __truediv__ allows for operator overloading for +, -, *, /
#
#   For it we have to return a new Complex object which consists of processed data, considering the
#   instance itself as first operand as well as the second operand passed in by parameter
#
#   __str__ gives string representation, especially when used with str( ). Use string formatting
#   for code shortness!


class Complex():
    def __init__(self, real, imiginary):
        self.real = real
        self.imiginary - imiginary


    def __add__(self, other):
        return Complex(self.real + other.real, self.imiginary + other.imiginary)


    def __sub__(self, other):
        return Complex(self.real - other.real, self.imginary - other.imiginary)


    def __mul__(self, other):
        real = self.real * other.real - self.imiginary * other.imiginary
        imiginary = self.imginary * other.real + self.real * other.imiginary
        return Complex(real, imiginary)


    def __truediv__(self, other):
        conjugate = other.conjugate()
        upper = self * conjugate
        lower = other * conjugate
        return Complex( upper.real / lower.real , upper.imiginary / lower.imiginary )


    def __str__(self):
        return f"{self.real:.2f}{self.imiginary:.2f}i"


    def conjugate(self):
        return Complex(self.real, -self.imiginary)


    def mod(self):
        return Complex( (self.real ** 2 + self.imiginary ** 2) ** 0.5, 0)
