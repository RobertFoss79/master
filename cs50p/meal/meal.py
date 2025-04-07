def main():
    time_input = input("Enter the time in 24-hour format: ")

    time_in_hours = convert(time_input)

    if 7 <= time_in_hours <=8:
        print("breakfast time")
    elif 12 <= time_in_hours <=13:
        print("lunch time")
    elif 18 <= time_in_hours <= 19:
        print("dinner time")


def convert(time: str) -> float:
    hours, minutes = map(int, time.split(":"))

    total_hours = hours + minutes / 60

    return total_hours


if __name__ == "__main__":
    main()
