import math

while True:
    try:
        x = int(input("Enter a number from 1 to 1000 to check if it is a perfect number: "))
        nums = set()
        if x < 1 or x > 1000:
            print("Out of range. Please enter a number between 1 and 1000")
        else:
            y = int(math.sqrt(x))
            for i in range(1, y + 1):
                if x % i == 0:
                    nums.add(i)
                    partner = x // i
                    if partner != i and partner != x:
                        nums.add(partner)
            total = sum(nums)
            if total == x:
                print(f"{x} is a perfect number")
                print(f"The divisors of {x} are: {sorted(nums)}")
            else:
                print(f"{x} is not a perfect number")
            again = input("Do you want to play again? (yes/no): ").strip().lower()
            if again != "yes":
                print("Goodbye. Thank you for playing")
                break

    except ValueError:
        print("Invalid input. Please enter a number between 1 and 1000: ")
