# Problem: Student Grades

# 1. Create a list called student_grades that contains the following grades: 85, 92, 78, 90, 88.

# 2. Print the entire list of grades.

# 3. Calculate and print the average grade.

# 4. Add a new grade 95 to the end of the list.

# 5. Remove the lowest grade from the list.

# 6 .Print the modified list and the new average grade.

student_grades = [85, 92, 78, 90, 88]
print(student_grades)

average_grade = sum(student_grades) / len(student_grades)
print(average_grade)

student_grades.append(95)

min_grade = min(student_grades)
student_grades.remove(min_grade)

print(student_grades)
