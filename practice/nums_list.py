# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# x = int(input("What is the number? "))
# if x in nums:
#     print("Found")
# else:
#     print("Not Found")
        
nums = list(range(1,11))
x = int(input("Choose a number from 1 to 10. "))
if x in nums:
    print(f"{x} is in the list of numbers")
else:
    print(f"{x} is not in the list of numbers")
