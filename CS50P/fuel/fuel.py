def main():
    while True:
        fraction = input("Enter your fuel level as a fraction: ")
        try:
            numerator, denominator = fraction.split("/")
            numerator = int(numerator)
            denominator = int(denominator)
            if numerator >= 0 and denominator > 0 and numerator <= denominator:
                break
            else:
                continue
        except (ValueError, ZeroDivisionError):
            continue


    percent = (numerator / denominator * 100)

    if percent < 2:
        print("E")
    elif percent >= 99:
        print("F")
    else:
        print(f"{int(round(percent))}%")

main()
