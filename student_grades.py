students = {}

name = input("Enter student name: ")
grade = input("Enter grade: ")
students[name] = grade

choice = input("Do you want to update a grade? (yes/no): ")

if choice.lower() == "yes":
    name = input("Enter student name to update: ")

    if name in students:
        grade = input("Enter new grade: ")
        students[name] = grade
        print("Grade updated successfully.")
    else:
        print("Student not found.")

print("\nAll Student Grades:")
for name, grade in students.items():
    print(name, ":", grade)