import inflect

p = inflect.engine()

names = []

def main():
    while True:
        try:
            user_name = input("Name: ").strip()
            names.append(user_name)
        except EOFError:
            term_exc()
            return False

def term_exc():
    adieu = p.join(names)
    print(f"Adieu, adieu, to {adieu}")

main()
