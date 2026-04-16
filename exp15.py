# Aim = Use of Python Debugger
# Coder = Mayuresh Mene
# Class = F.E.Computers 1
# UIN/Roll no = 251P016 / 15
# Date = 
import pdb
pdb.set_trace()

def calculate_average(numbers):
    total = 0
    for num in numbers:
        total += num
    
    average = total / (len(numbers) - 1)
    return average

nums = [10, 20, 30, 40]
print("Average:", calculate_average(nums))