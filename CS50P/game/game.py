import random

def main():
    random_num = random.randint(1, 100)
    while True:
        try:
            user_level = int(input("Level: "))
            if user_level < 1:
                continue
            else:
                break
        except ValueError:
            pass

    while True:
        try:
            user_guess = int(input("Guess: "))
            if user_guess < 1:
                continue
            elif user_guess < random_num:
                print("Too small!")
            elif user_guess > random_num:
                print("Too large!")
            elif user_guess == random_num:
                print("Just right!")
                break
        except ValueError:
            pass


if __name__ == "__main__":
    main()
