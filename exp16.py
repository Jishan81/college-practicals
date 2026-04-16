# Aim = Use of Regular Expressions
# Coder = Mayuresh Mene
# Class = F.E.Computers 1
# UIN/Roll no = 251P016 / 15
# Date = 
import re

# Function to validate phone number
def validate_phone(phone):
    # Accepts formats like: 9876543210, +919876543210, 09876543210
    pattern = r'^(\+91[\-\s]?)?[0]?[6-9]\d{9}$'
    return re.match(pattern, phone)

# Function to validate email
def validate_email(email):
    # Standard email format
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email)

# Main program
phone = input("Enter your phone number: ")
email = input("Enter your email ID: ")

# Validate phone
if validate_phone(phone):
    print("Valid phone number ✅")
else:
    print("Invalid phone number ❌")

# Validate email
if validate_email(email):
    print("Valid email ID ✅")
else:
    print("Invalid email ID ❌")