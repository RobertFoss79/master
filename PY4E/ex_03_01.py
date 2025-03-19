hours = input("Enter Hours: ")
rate = input("Enter Rate: ")
fh = float(hours)
fr = float(rate)
if fh > 40:
    reg_pay = fr * 40
    ot_pay = (fh - 40) * (fr * 1.5)
    print(reg_pay + ot_pay)
else:
    pay = fh * fr
    print("Pay:", pay)