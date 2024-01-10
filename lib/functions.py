#!/usr/bin/env python3

def greet_programmer():
    print("Hello, programmer!")
#Call it
greet_programmer()


def greet(name):
    print(f"Hello, {name}!")

# calling the return value
greet("Naureen")



import io
import sys

def greet_with_default(name="programmer"):
    greeting = f"Hello, {name}!"
    print(greeting)
    return greeting

# Example usage
result_1 = greet_with_default()
result_2 = greet_with_default("Sunny")

# Test
assert greet_with_default("Guido") == "Hello, Guido!"

# Additional test
def test_greet_with_default_with_param():
    '''prints "Hello, {name}!"'''
    captured_out = io.StringIO()
    sys.stdout = captured_out
    greet_with_default("Guido")
    sys.stdout = sys.__stdout__
    assert captured_out.getvalue() == "Hello, Guido!\n"

# Run the additional test
test_greet_with_default_with_param()





def add(num1, num2):
    return num1+num2
#calling the numbers
result= add(1,2)
print("add:",result)


def halve(number):
    # if statements  If the condition in the if statement is true (meaning number is not a number), the function returns None&If the condition in the if statement is false (meaning number is a number), the function returns half of the input number. 
    if not isinstance(number, (int, float)):
        return None

    return number / 2

# calling the numbers and # calling the string hence not a number
result = halve(4)
print(result)  

result = halve("two")
print(result)  



