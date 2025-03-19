class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError("Missing name")
        self.name = name
        self.house = house


def main():
    student = get_student()
    print(f"{student.name} from {student.house}")


def get_student():
    name = input("Name: ")
    house = ("House: ")
    try:
        return Student(name, house)
    except Value:
        ...
    

if __name__ == "__main__":
    main()
