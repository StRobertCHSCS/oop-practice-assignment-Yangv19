# Define your Fraction class here
class Fraction:

    def __init__(self, numerator, denominator):

        if denominator == 0:
            raise ValueError("Denominator cannot be zero")

        self.numerator = numerator
        self.denominator = denominator

    def get_numerator(self):
        return self.numerator

    def get_denominator(self):
        return self.denominator

    def set_numerator(self, new_numerator):
        self.numerator = new_numerator

    def set_denominator(self, new_denominator):

        if new_denominator == 0:
            raise ValueError("Denominator cannot be zero")

        self.denominator = new_denominator

    def __str__(self):
        self.__reduce()
        return str(self.numerator) + "/" + str(self.denominator)

    def add(self, other_fraction):
        self.numerator = (self.numerator * other_fraction.denominator) + (other_fraction.numerator * self.denominator)
        self.denominator = self.denominator * other_fraction.denominator

    def subtract(self, other_fraction):
        self.numerator = (self.numerator * other_fraction.denominator) - (other_fraction.numerator * self.denominator)
        self.denominator = self.denominator * other_fraction.denominator

    def multiply(self, other_fraction):
        self.numerator = self.numerator * other_fraction.numerator
        self.denominator = self.denominator * other_fraction.denominator

    def __reduce(self):
        lcm = 1
        i = 2
        while i < self.denominator:
            if self.numerator % i == 0 and self.denominator % i == 0:
                lcm = i
            i = i + 1

        self.numerator = int(self.numerator / lcm)
        self.denominator = int(self.denominator / lcm)


if __name__ == '__main__':
    num = int("Enter the numerator: ")
    denom = int("Enter the denominator: ")

    num2 = int("Enter the numerator: ")
    denom2 = int("Enter the denominator: ")

    fraction1 = Fraction(num, denom)
    fraction2 = Fraction(num2, denom2)

    print(str(fraction1) + " + " + str(fraction2) + " = " + str(fraction1.add(fraction2)))
    print(str(fraction1) + " - " + str(fraction2) + " = " + str(fraction1.subtract(fraction2)))
    print(str(fraction1) + " * " + str(fraction2) + " = " + str(fraction1.multiply(fraction2)))

    pass
