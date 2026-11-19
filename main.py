from student import *

# List of students and their grades
students = {
    "Ali": [15, 20, 18, 17],
    "Sara": [19, 18, 20, 17],
    "Reza": [8, 12, 9, 10],
    "Maryam": [14, 16, 13, 15],
}

# Get the student's name from the user
name = input("Enter student name: ").strip().capitalize()

if name in students:
    student_grades = students[name]
    average = avg(student_grades)

    print()
    print("student:", name)
    print("Avg =", round(average, 2))
    print("max =", max_grade(student_grades))
    print("min =", min_grade(student_grades))
    print("status =", check_status(average))
else:
    print("Student not found!")
    print("Students:", ", ".join(students))
