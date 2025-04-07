import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip_address):
    if re.search(r"^(([0-9]?[0-9]|[0-1]?[0-9]?[0-9]|24[0-9]|[0-2]?[0-5]?[0-5])\.){3}"
                 r"([0-9]?[0-9]|[0-1]?[0-9]?[0-9]|24[0-9]|[0-2]?[0-5]?[0-5])$", ip_address):
        return True
    else:
        return False


if __name__ == "__main__":
    main()
