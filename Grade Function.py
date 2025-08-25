def gradeFunction():
    grade = int(input("Please enter your grade:"))
    if grade < 60:
        score = "F"
    elif grade < 70:
        score = "D"
    elif grade < 80:
        score = "C"
    elif grade < 90:
        score = "B"
    else:
        score = "A"
    print(f"With a grade of {grade} you got {score}.")

gradeFunction()
gradeFunction()
gradeFunction()