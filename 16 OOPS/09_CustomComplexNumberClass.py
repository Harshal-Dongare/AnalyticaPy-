class ComplexNumber:
    def __init__(self, real=0.0, imag=0.0):
        self.imag = float(imag)
        self.real = float(real)

    def __str__(self):
        # If real part is 0
        if self.real == 0:
            return f"{int(self.imag) if self.imag.is_integer() else self.imag}i"
        # if imaginary part is -ve
        elif self.imag < 0:
            s = f"{(int(self.real) if self.real.is_integer() else self.real)}{(int(self.imag) if self.imag.is_integer() else self.imag)}i"
        # if imaginary part is positive
        else:
            s = f"{(int(self.real) if self.real.is_integer() else self.real)}+{(int(self.imag) if self.imag.is_integer() else self.imag)}i"
        return s 

    def __add__(self, other):
        real_part = 0
        imag_part = 0

        real_part = self.real + other.real
        imag_part = self.imag + other.imag

        ans = ComplexNumber(real_part, imag_part)
        return ans

    def __sub__(self, other):
        real_part = 0
        imag_part = 0

        real_part = self.real - other.real
        imag_part = self.imag - other.imag

        ans = ComplexNumber(real_part, imag_part)
        return ans

    def __mul__(self, other):
        real_part = 0
        imag_part = 0

        real_part = (self.real * other.real) - (self.imag * other.imag)
        imag_part = (self.real * other.imag) + (self.imag * other.real)

        ans = ComplexNumber(real_part, imag_part)
        return ans

    def __truediv__(self, other):
        real_part = 0
        imag_part = 0
        den = (other.real**2) + (other.imag**2)

        ans = self * ComplexNumber((other.real/den), (-1*other.imag)/den)
        return ans

    def __eq__(self, other):
        return (self.real == other.real and self.imag == other.imag)

    def __neq__(self, other):
        return (self.real != other.real and self.imag != other.imag)

    def conjugate(self):
        real_num = int(self.real) if self.real.is_integer() else self.real
        imag = int(self.imag * -1) if self.imag.is_integer() else (self.imag * -1)
        return ComplexNumber(real_num, imag)


# Two complex number class objects
cn1 = ComplexNumber(3,4)
cn2 = ComplexNumber(3,5)

# Print individual complex number using __str__dunder method
print(cn1)              # Output: 3+4i
print(cn2)              # # Output: 3+5i

# conjugate instance method
print(cn1.conjugate())

# Addition of two complex nums using __add__ dunder method
print(cn1 + cn2)

# Subtraction of two complex nums using __sub__ dunder method
print(cn1 - cn2)

# Multiplication of two complex nums using __mul__ dunder method
print(cn1 * cn2)

# Division of two complex nums using __truediv__ dunder method
print(cn1 / cn2)

# Check equality of two complex nums using __eq__ dunder method
print(cn1 == cn2)

# Check in-equality of two complex nums using __neq__ dunder method
print(cn1 != cn2)
