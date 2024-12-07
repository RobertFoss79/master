from datetime import datetime


class Expense:
    def __init__(self, amount=0.0, date=None):
        self.amount = amount
        self.date = date or datetime.now().strftime("%Y-%m-%d")

    def input_expense(self):
        while True:
            try:
                self.amount = float(
                    input(f"Enter {self.__class__.__name__.lower()} expense: ")
                )
                self.amount = round(self.amount, 2)
                break
            except ValueError:
                print("Invalid input. Please enter a numeric value")
        self.date = (
            input("Enter the date (YYYY-MM-DD) or leave blank for today: ") or self.date
        )
        return self.amount, self.date


class Rent(Expense):
    def __init__(self, amount=0.0, date=None):
        self.amount = amount
        self.date = date or datetime.now().strftime("%Y-%m-%d")

    def input_expense(self):
        self.amount = float(input("Enter your rent amount: "))
        self.date = (
            input("Enter the date (YYYY-MM-DD) or leave blank for today: ") or self.date
        )
        return self.amount, self.date


class PowerGas(Expense):
    def __init__(self, amount=0.0, date=None):
        self.amount = amount
        self.date = date or datetime.now().strftime("%Y-%m-%d")

    def input_expense(self):
        self.amount = float(input("Enter your Power/Gas amount: "))
        self.date = (
            input("Enter the date (YYYY-MM-DD) or leave blank for today: ") or self.date
        )
        return self.amount, self.date


class WaterSewerTrash(Expense):
    def __init__(self, amount=0.0, date=None):
        self.amount = amount
        self.date = date or datetime.now().strftime("%Y-%m-%d")

    def input_expense(self):
        self.amount = float(input("Enter your Water/Sewer/Trash amount: "))
        self.date = (
            input("Enter the date (YYYY-MM-DD) or leave blank for today: ") or self.date
        )
        return self.amount, self.date


class Gasoline(Expense):
    def __init__(self, amount=0.0, date=None):
        self.amount = amount
        self.date = date or datetime.now().strftime("%Y-%m-%d")

    def input_expense(self):
        self.amount = float(input("Enter your Gasoline amount: "))
        self.date = (
            input("Enter the date (YYYY-MM-DD) or leave blank for today: ") or self.date
        )
        return self.amount, self.date


class CarInsurance(Expense):
    def __init__(self, amount=0.0, date=None):
        self.amount = amount
        self.date = date or datetime.now().strftime("%Y-%m-%d")

    def input_expense(self):
        self.amount = float(input("Enter your Car Insurance amount: "))
        self.date = (
            input("Enter the date (YYYY-MM-DD) or leave blank for today: ") or self.date
        )
        return self.amount, self.date


class CarPayment(Expense):
    def __init__(self, amount=0.0, date=None):
        self.amount = amount
        self.date = date or datetime.now().strftime("%Y-%m-%d")

    def input_expense(self):
        self.amount = float(input("Enter your Car Payment amount: "))
        self.date = (
            input("Enter the date (YYYY-MM-DD) or leave blank for today: ") or self.date
        )
        return self.amount, self.date


class Phone(Expense):
    def __init__(self, amount=0.0, date=None):
        self.amount = amount
        self.date = date or datetime.now().strftime("%Y-%m-%d")

    def input_expense(self):
        self.amount = float(input("Enter your Phone amount: "))
        self.date = (
            input("Enter the date (YYYY-MM-DD) or leave blank for today: ") or self.date
        )
        return self.amount, self.date


class Internet(Expense):
    def __init__(self, amount=0.0, date=None):
        self.amount = amount
        self.date = date or datetime.now().strftime("%Y-%m-%d")

    def input_expense(self):
        self.amount = float(input("Enter your Internet amount: "))
        self.date = (
            input("Enter the date (YYYY-MM-DD) or leave blank for today: ") or self.date
        )
        return self.amount, self.date


class Groceries(Expense):
    def __init__(self, amount=0.0, date=None):
        self.amount = amount
        self.date = date or datetime.now().strftime("%Y-%m-%d")

    def input_expense(self):
        self.amount = float(input("Enter your Groceries amount: "))
        self.date = (
            input("Enter the date (YYYY-MM-DD) or leave blank for today: ") or self.date
        )
        return self.amount, self.date


class Household(Expense):
    def __init__(self, amount=0.0, date=None):
        self.amount = amount
        self.date = date or datetime.now().strftime("%Y-%m-%d")

    def input_expense(self):
        self.amount = float(input("Enter your Household Expense amount: "))
        self.date = (
            input("Enter the date (YYYY-MM-DD) or leave blank for today: ") or self.date
        )
        return self.amount, self.date


class Hygiene(Expense):
    def __init__(self, amount=0.0, date=None):
        self.amount = amount
        self.date = date or datetime.now().strftime("%Y-%m-%d")

    def input_expense(self):
        self.amount = float(input("Enter your Hygiene Expense amount: "))
        self.date = (
            input("Enter the date (YYYY-MM-DD) or leave blank for today: ") or self.date
        )
        return self.amount, self.date
