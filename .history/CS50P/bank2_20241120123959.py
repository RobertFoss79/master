# Global Variables

balance = 0


def main():
    balance = 0
    print("Balance:", balance)
    deposit(100)
    withdraw(50)
    print("Balance:", balance)

def deposit(n):
    balance += n

def withdraw(n):
    balance -= n


if __name__ == "__main__":
    main()
