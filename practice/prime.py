import math

while True:
    try:
        x = int(input("Enter a number between 1 and 100 to check if it is a prime number: "))
        if x < 1 or x > 100:
            print("Out of range. Please enter a number between 1 and 100 to check if it is a prime number: ")
        elif x == 1:
            print(f"{x} is not a prime number")
        else:
            y = int(math.sqrt(x))
            for i in range(2, y + 1):
                if x % i == 0:
                    print(f"{x} is divisible by {i}, so it is not a prime number.")
                    break
            else:
                print(f"{x} is a prime number")
            again = input("Do you want to play again? (yes/no): ").strip().lower()
            if again != "yes":
                print("Goodbye, thank you for playing.")
                break
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 100 to check if it is a prime number: ")