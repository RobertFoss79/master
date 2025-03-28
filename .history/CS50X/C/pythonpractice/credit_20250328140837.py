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


# #include <cs50.h>
# #include <ctype.h>
# #include <stdio.h>
# #include <string.h>

# // Function prototypes
# int is_all_digits(const char* str);
# int validate_card(long number);
# char* get_card_type(long number);

# int main(void)
# {
#     // Prompt user for input
#     long number;
#     char str[16]; // Buffer to store the number with a maximum length of 16 digits
#     do
#     {
#         number = get_long("What is your card number? ");
#         sprintf(str, "%ld", number); // Convert number to string
#     }
#     while (!is_all_digits(str)); // Pass the string to is_all_digits
# }


# // Function Definitions
# // Check that the card number is all digits with no spaces, dashes, or letters
# int is_all_digits(const char* str) {
#     for (int i = 0; i < strlen(str); i++) {
#         if (!isdigit(str[i])) {
#             return 0; // Not all digits
#         }
#     }
#     return 1; // All digits
# }

# // Validate that the card is an actual card number
# int validate_card(long number)
# {

# }

# // Determine the card type
# char* get_card_type(long number)
# {

}
}
