cost_of_coke = 50

amount_due = cost_of_coke


while amount_due > 0:

    coin = int(input("Insert Coin: "))

    if coin in [5, 10, 25]:

        amount_due -= coin

        if amount_due > 0:
            print(f"Amount Due: {amount_due}")
        elif amount_due == 0:
            print(f"Change Owed: {amount_due}")
        elif amount_due < 0:
            print(f"Change Owed: {abs(amount_due)}")
    else:
        print(f"Amount Due: {amount_due}")
