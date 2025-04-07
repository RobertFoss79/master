from PIL import Image, ImageOps
import os, sys

def main():
    arg_validity_check()
    check_file()
    shirt_fit()

def arg_validity_check():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif not os.path.isfile(sys.argv[1]):
        sys.exit("Invalid input - Path")


def check_file():
    formats: list[str] = ["jpg", "jpeg", "png"]
    index_1: any = formats.index(sys.argv[1].split(".")[1])
    index_2: any = formats.index(sys.argv[2].split(".")[1])

    if index_1 is None or index_2 is None:
        sys.exit("Invalid input")
    if index_2 != index_1:
        sys.exit("Input and output have different extensions")

def shirt_fit():
    shirt = Image.open("shirt.png")
    image = Image.open(sys.argv[1])
    image = ImageOps.fit(image, shirt.size)
    image.paste(shirt, shirt)
    image.save(sys.argv[2])

if __name__ == "__main__":
    main()
