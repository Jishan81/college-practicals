# AIM: Using function, write a Python program 
# to analyze the input number is prime or not.
# Coder: Adi
# Date: 02-02-2026

print("--- Prime Number Analyzer ---\n")


# Implement the below function such that it returns True if n is prime, else False
def is_prime(n):
    if n<=1:
        return False
    for a in range(2,n):
        if n%a==0:
            return False
    return True

# Do not chage the code below
n = int(input("Enter a number: "))
if is_prime(n):
    print(f"{n} is a Prime Number.")
else:
    print(f"{n} is NOT a Prime Number.")

# End of the program