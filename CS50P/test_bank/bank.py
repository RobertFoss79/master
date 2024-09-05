def main():
    user_greeting = input("What is your greeting? ").strip().lower()
    result = value(user_greeting)
    print(f"${result}")


def value(greeting):
    greeting = greeting.lower()
    if "hello" in greeting:
        return 0
    elif greeting.startswith("h") and greeting != "hello":
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()
