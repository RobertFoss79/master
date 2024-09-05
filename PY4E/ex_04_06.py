def computepay(hours, rate):
    print("In computepay", hours, rate)
    if hours > 40:
        reg_pay = rate * hours
        ot_pay = (hours - 40) * (rate * 0.5)
        pay = reg_pay + ot_pay
    else:
        pay = hours * rate
    print("Returning", pay)
    return pay

hours = input("Enter Hours: ")
rate = input("Enter Rate: ")
fh = float(hours)
fr = float(rate)

xp = computepay(fh, fr)

print("Pay:", xp)