# Bismillahir Rahmanir Rahim
# Nafis Khan Chowdhury
# Calculator with Constructor





class Calculator:
    # this is a calculator class

    def __init__(self, a, b):
        # this is a constructor class
        self.a = a
        self.b = b

    def add(self):
        # method for addition
        return self.a + self.b

    def subtract(self):
        # method for subtraction
        return self.a - self.b

    def multiply(self):
        # method for multiplication
        return self.a * self.b

    def divide(self):
        # method for division
        try:
            return self.a / self.b
        except ZeroDivisionError:
            return 'cannot divided by zero'


my_calculator = Calculator(5, 3)

print(my_calculator.add())
print(my_calculator.subtract())
print(my_calculator.multiply())
print(my_calculator.divide())