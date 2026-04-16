# AIM: Task List Manager
# Coder: jishan
# Date: 29-01-26

print("--- Task List Manager ---")
tasks = ["Sleep", "Getup", "Brush"]
print(f"Original Tasks: {tasks}")

# Write your code here
# Add new task
a = input("Enter a new task to add: ")
tasks.append(a)
print("Tasks after Adding:",tasks)

#Update a Task
c = int(input("Enter the index of the task to edit: "))
d = input("Enter the new task: ")
tasks[c] = d
print("Tasks after Editing:",tasks)

# Remove a task
b = int(input("Enter the index of the task to remove: "))
tasks.pop(b)
print("Tasks after Removing:",tasks)

# Sort a Task
tasks.sort()
print("Tasks after Sorting:",tasks)