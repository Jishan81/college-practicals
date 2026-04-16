
# AIM: Write a Python program to calculate the gross salary of an employee.
# Coder:jishan
# Date:16 JAN2026

# Write your code here:
BS=int(input("Enter Basic Salary:"))
DA=BS*0.7
TA=BS*0.3
HRA=BS*0.1

print("Salary Details:")
print("YOUR BASIC SALARY IS:",BS)
print(" DA(70%)\t",DA)
print(" TA(30%)\t",TA)
print(" HRA(10%)\t",HRA)
print(" Gross Salary:\t",BS+DA+HRA+TA)