# Student Project

A small Python project that shows a student's average, highest and lowest grade, and whether they passed.

## Structure

```
student_project/
├── main.py            # gets the student's name, holds the grades list, calls the functions
└── student/
    ├── __init__.py    # imports everything from grades and status
    ├── grades.py      # avg, max_grade, min_grade
    └── status.py      # check_status: ACC if average > 10, otherwise REJ
```

## Run

```
python main.py
```

## Example

```
Enter student name: Ali

student: Ali
Avg = 17.5
max = 20
min = 15
status = ACC
```
