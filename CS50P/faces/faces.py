def main():
    print(converted_greeting)


def convert(greeting):
    greeting = greeting.replace(":)", "🙂")
    greeting = greeting.replace(":(", "🙁")
    return greeting

original_greeting = input("What is your greeting? ")

converted_greeting = convert(original_greeting)


main()
