import sys
import random
from pyfiglet import Figlet, FontNotFound

def main():
    args = sys.argv[1:]
    font_name = None

    if len(args) == 2 and args[0] in ("-f", "--font"):
        font_name = args[1]
    elif len(args) != 0:
        sys.exit("Invalid usage")

    if font_name is None:
        fonts = Figlet().getFonts()
        font_name = random.choice(fonts)

    try:
        figlet = Figlet(font=font_name)
    except FontNotFound:
        sys.exit("Invalid usage")

    user_input = input("Enter the text you want to figletize: ")
    print(figlet.renderText(user_input))

if __name__ == "__main__":
    main()
