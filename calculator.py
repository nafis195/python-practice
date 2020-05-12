# Bismillahir Rahmanir Rahim
# Nafis Khan Chowdhury
# calculator.py




class Calculator:
    # this is a calculator class

    def add(self, a, b):
        # function for addition
        return a+b
    
    def subtract(self, a, b):
        # function for subtraction
        return a-b
    
    def multiply(self, a, b):
        # function for multiplication
        return a*b

    def divide(self, a, b):
        # function for division
        try:
            return a/b
        except ZeroDivisionError:
            return 'It is impossible to divide by zero.'


my_calculator = Calculator()

temp = my_calculator.add(5, 3)
print(temp)

temp = my_calculator.subtract(5, 3)
print(temp)

temp = my_calculator.multiply(5, 3)
print(temp)

temp = my_calculator.divide(5, 3)
print(temp)

temp = my_calculator.divide(5, 0)
print(temp)