# 1
# # name = input("Name: ")
# house = input("House: ")
# print(F"{name} from {house}")



# 2
# def main():
#     name = get_name()
#     house = get_house()
#     print(f"{name} from {house}")


# def get_name():
#     return input("Name: ")

# def get_house():
#     return input("House: ")
    

# if __name__ == "__main__":
#     main()




# 3
# def main():
#     name, house = get_student()
#     print(f"{name} from {house}")


# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
#     return name, house
    

# if __name__ == "__main__":
#     main()



# 4
def main():
    name, house = get_student()
    print(f"{name} from {house}")


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return name, house
    

if __name__ == "__main__":
    main()
