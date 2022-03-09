grades = []

grade = input("Enter the first grade: ")
grades.append(float(grade))

grade = input("Enter the second grade: ")
grades.append(float(grade))

grade = input("Enter the third grade: ")
grades.append(float(grade))

grade = input("Enter the fourth grade: ")
grades.append(float(grade))

grade = input("Enter the fifth grade: ")
grades.append(float(grade))

grades.sort()
grades = grades[2:]
grades = sum(grades)
result = grades/3
print("Average Grade: {0:.2f}%".format(result))