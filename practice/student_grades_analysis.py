# Problem: Student Grades Analysis

# 1. Create a list called grades with the following grades: 88, 76, 90, 85, 95, 83, 79, 92.

# 2. Print the entire list of grades.

# 3. Calculate and print the average grade.

# 4. Find and print the highest and lowest grades in the list.

# 5. Count and print the number of grades above the average grade.

# 6. Sort the list of grades in ascending order and print the sorted list.

grades = [88, 76, 90, 85, 95, 83, 79, 92]
print(grades)

average = sum(grades) / len(grades)
print (average)

max_grade = max(grades)
min_grade = min(grades)
print(max_grade, min_grade)

above_ave = []

for grade in grades:
    if grade > average:
        above_ave.append(grade)
print(len(above_ave), above_ave)

grades.sort()
print(grades)
