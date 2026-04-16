# AIM: Implement a simple Python calculator that takes user input and 
# performs basic arithmetic operations (addition, subtraction, 
# multiplication, division) using functions.
# Coder: jishan
# Date: 02-02-2026

import calculator

print("--- Calculator ---\n")

# Write Your Code Here. And write the Calculator functions in calculator.py file.
import calculator

num1 = float(input())
num2 = float(input())
ope = input('')

if ope == "+":
    print(f"{num1} + {num2} = {calculator.add(num1,num2)}")
    
elif ope == "-":
    print(f"{num1} - {num2} = {calculator.subtract(num1,num2)}")
    
elif ope == "*":
    print(f"{num1} * {num2} = {calculator.multiply(num1,num2)}")
    
elif ope == "/":
    print(f"{num1} / {num2} = {calculator.divide(num1,num2)}")
    
else:
    print(f"Invalid Selection!!!")
    def add(num1,num2):
    return num1 + num2

def subtract(num1,num2):
    return num1 - num2

def multiply(num1,num2):
    return num1 * num2

def divide(num1,num2):
    if num2 == 0:
        return ("Not Defined")
    else:
        return num1 / num2