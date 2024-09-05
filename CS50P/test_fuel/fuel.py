def main():
    while True:
        fraction = input("Enter your fuel level as a fraction: ").strip()
        try:
            percentage = convert(fraction)
            break
        except (ValueError, ZeroDivisionError):
            continue

    print(gauge(percentage))

def convert(fraction):
    try:
        numerator, denominator = map(int, fraction.split("/"))
    except ValueError:
        raise ValueError("Invalid input format. Please use X/Y format.")

    if denominator == 0:
        raise ZeroDivisionError("Denominator cannot be zero.")

    if numerator < 0 or denominator <= 0 or numerator > denominator:
        raise ValueError("Invalid fraction. X must be between 0 and Y.")

    return round(numerator / denominator * 100)

def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"

if __name__ == "__main__":
    main()
