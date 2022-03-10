'''
**********English**********
Start
create a list to store 5 numbers (decimal)
capture user's input 5 times for their grades
each time we capture the user's input, we append the number to the list
sort the list in ascending order, then splice the item starting at index 2
once we have 3 highest numbers in the list, we sum them up and divide by 3
output a message to the user

end


**********pseudocode**********
create list

capture input
append 1st number to list

capture input
append 2nd number to list

capture input
append 3rd number to list

capture input
append 4th number to list

capture input
append 5th number to list

print message to user
'''
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