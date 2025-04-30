# nums = list(range(1,21))
# x = int(input("Please give a number between 1 and 20 "))
# if x in nums and x % 2 == 0:
#     print(f"{x} is an even number in the list.")
# elif x in nums and x % 2 != 0:
#     print(f"{x} is an odd number in the list.")
# else:
#     print(f"{x} is not in the list.")
 

nums = list(range(1, 21))

while True:
    try:
        x = int(input("Enter a number between 1 and 20. "))
        if x in nums:
            if x % 2 == 0:
                print(f"{x} is an even number in the list")
            else:
                print(f"{x} is an odd number in the list.")
        else:
            print(f"{x} is not in the list.")
        again = input("Do you want to play again? (yes/no): ").strip().lower()
        if again != "yes":
            print("Goodbye, thank you for playing.")
            break
    except ValueError:
        print("Invalid input. Please enter a number from 1 to 20.")
