def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(dollars_str):
    dollars_str = dollars_str[1:]
    amount_float = float(dollars_str)
    return amount_float


def percent_to_float(percent_str):
    percent_str = percent_str[:-1]
    percent_float = float(percent_str) / 100
    return percent_float



main()
