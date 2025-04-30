# nums = list(range(1, 51))

# while True:
#     try:
#         x = int(input("Enter a number from 1 to 50 to check divisibility by 3 and/or 5: "))
#         if x in nums:
#             if x % 3 == 0 and x % 5 == 0:
#                 print("Fizzbuzz")
#             elif x % 3 == 0:
#                 print("Fizz")
#             elif x % 5 == 0:
#                 print("Buzz")
#             else:
#                 print("Number is not divisible by 3 or 5")
#             again = input("Do you want to play again? (yes/no): ").strip().lower()
#             if again != "yes":
#                 print("Goodbye, thank you for playing.")
#                 break
#     except ValueError:
#         print("Invalid input, please enter a number between 1 and 50 that is divisible by 3 and/or 5")


nums = list(range(1, 51))

while True:
    try:
        x = int(input("Enter a number from 1 to 50 to check divisibility by 3 and/or 5: "))
        if x in nums:
            if x % 3 == 0 and x % 5 == 0:
                print(f"{x} is divisible by 3 and 5: Fizzbuzz")
            elif x % 3 == 0:
                print(f"{x} is divisible by 3: Fizz")
            elif x % 5 == 0:
                print(f"{x} is divisible by 5: Buzz")
            else:
                print(f"{x} is not divisible by 3 or 5")
            again = input("Do you want to play again? (yes/no): ").strip().lower()
            if again != "yes":
                print("Goodbye, thank you for playing.")
                break
        else:
            print("Number is out of range. Please enter a number from 1 to 50 to check divisibility by 3 and/or 5: ")
    except ValueError:
        print("Invalid input, please enter a number between 1 and 50 that is divisible by 3 and/or 5")
