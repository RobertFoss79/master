from datetime import datetime


class Income:
    def __init__(self, amount=0.0, date=None):
        self.amount = amount
        self.date = date or datetime.now().strftime("%Y-%m-%d")

    def input_income(self):
        while True:
            try:
                self.amount = float(
                    input(f"Enter {self.__class__.__name__.lower()} income: ")
                )
                self.amount = round(self.amount, 2)
                break
            except ValueError:
                print("Invalid Input. Please enter a numeric value.")
        self.date = (
            input("Enter the date (YYYY-MM-DD) or leave blank for today: ") or self.date
        )
        return self.amount, self.date


class PayrollIncome(Income):
    def __init__(self, amount=0.0, date=None):
        self.amount = amount
        self.date = date or datetime.now().strftime("%Y-%m-%d")

    def input_income(self):
        self.amount = float(input(f"Enter {self.__class__.__name__.lower()} income: "))
        self.date = (
            input("Enter the date (YYYY-MM-DD) or leave blank for today: ") or self.date
        )
        return self.amount, self.date


class OtherIncome(Income):
    def __init__(self, amount=0.0, date=None):
        self.amount = amount
        self.date = date or datetime.now().strftime("%Y-%m-%d")

    def input_income(self):
        self.amount = float(input(f"Enter {self.__class__.__name__.lower()} income: "))
        self.date = (
            input("Enter the date (YYYY-MM-DD) or leave blank for today: ") or self.date
        )
        return self.amount, self.date
