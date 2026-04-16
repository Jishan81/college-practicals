#Aim : Create a Python code to demonstrate the use of sets and perform set operations (union, intersection, difference) to manage student enrollments in multiple courses / appearing for multiple entrance exams like CET, JEE, NEET etc.
#Name : jishan
#Class : FE COMPS
#Date : 29|01|26

#USE OF SETS

print("--- Entrance Exam Students ---")
print("List Of Students :")
CET = {'Bob', 'Frank', 'Charlie', 'Alice'}
print("CET Students:",CET)
JEE = {'Bob', 'Heidi', 'Frank', 'Eve'}
print("JEE Students:",JEE)
NEET = {'Bob', 'Charlie', 'Karl', 'Liam'}
print("NEET Students:",NEET)
STUDENTS = JEE.union(NEET,CET)
print("All Students:",STUDENTS)
EXAMS = JEE.intersection(NEET,CET)
print("All Exams:",EXAMS)
JEE_NEET = JEE - NEET
print("JEE but not for NEET",JEE_NEET)
CET_NEET = CET.intersection(NEET) - JEE
print("CET and NEET but not for JEE:",CET_NEET)