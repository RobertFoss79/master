from datetime import date, timedelta
import sys, inflect

p = inflect.engine()

def main():
    try:
        year, month, day = input("Date of Birth: ").split("-")
        year, month, day = int(year), int(month), int(day)
    except ValueError:
        sys.exit("Invalid Date")

    print(convert_to_minutes(year, month, day))


def convert_to_minutes(year: int, month: int, day: int):
    try:
        today: date = date.today()

        diff: timedelta = today - date(year, month, day)
    except ValueError:
        sys.exit("Invalid Date")

    minutes: int = diff.days * 24 * 60

    return f"{p.number_to_words(minutes, andword='')} minutes".capitalize()

if __name__ == "__main__":
    main()
