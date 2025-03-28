def validate_card(number):
    # Convert number to string to access digits
    card_number = str(number)
    total = 0
    
    # Reverse the card number for easier index-based processing
    reversed_digits = card_number[::-1]
    
    # Process digits
    for i, digit in enumerate(reversed_digits):
        n = int(digit)
        if i % 2 == 1:  # Double every second digit
            n *= 2
            if n > 9:  # If result has two digits, add them
                n -= 9
        total += n

    # If total modulo 10 is 0, the card is valid
    return total % 10 == 0


def get_card_type(number):
    card_number = str(number)
    
    if card_number.startswith(("34", "37")) and len(card_number) == 15:
        return "AMEX"
    elif card_number.startswith(tuple(str(i) for i in range(51, 56))) and len(card_number) == 16:
        return "MASTERCARD"
    elif card_number.startswith("4") and len(card_number) in {13, 16}:
        return "VISA"
    else:
        return "INVALID"


# Main function to prompt user for input
def main():
    number = input("Number: ")
    if not number.isdigit():
        print("INVALID")
        return
    
    if validate_card(number):
        print(get_card_type(number))
    else:
        print("INVALID")


if __name__ == "__main__":
    main()
