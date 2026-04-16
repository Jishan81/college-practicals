# AIM: Write a Python program that takes two 
# numbers as input and performs division. 
# Implement exception handling to manage division 
# by zero and invalid input errors gracefully.
# Coder: Mayuresh Mene
# Date: 16-02-2026

try:
    num1 = float(input("Enter first number(Dividend): "))
    num2 = float(input("Enter second number(Divisor): "))
    div = num1 / num2
    print(f"The result of {num1} divided by {num2} is: {div}")
    # True and correct code that may cause error
except ValueError:
    print("Error: Invalid input. Please enter numeric values.")
    # Except - code to handle error
except ZeroDivisionError:
    print("Error: You cannot divide by zero.")
    # Except - code to handle error
except:
    print("Some error occured!")
    # Except - code to handle error
else:
    print("Division performed successfully.")
finally:
    print("Program execution completed.")