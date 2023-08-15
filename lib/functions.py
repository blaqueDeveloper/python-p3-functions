#!/usr/bin/env python3

def my_function(param):
    print("Running my_function")
    return param + 1

my_function_return_value = my_function(1)
print(my_function_return_value)

def greet_programmer():
    print("Hello, programmer!")

def greet(name):
    print(f"Hello, {name}!")

def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")

def add(num1, num2):
    sum = num1 + num2
    return sum

def halve(number):
    half = number * 0.5
    return half
