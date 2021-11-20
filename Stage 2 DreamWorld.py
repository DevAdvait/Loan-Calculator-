principal = int(input("Enter the loan principal: "))

mode = str(input("What do you want To Calculate?\n"
                 "type 'm' for number of monthly payments\n"
                 "type 'p' for the monthly payment\n"))

if mode == "m" or mode == "M":
    monthly_payment = int(input("Enter Monthly Payment: "))
    months = -(-principal // monthly_payment)
    if months > 1:
        print("It will take %d months to complete the payment." % int(months))
    else:
        print("It will take %d month to complete the payment." % int(months))
elif mode == "p" or mode == "P":

    months = int(input("Enter Number of Months: "))
    amount = -(-principal // months)
    last_payment = principal - ((months - 1) * amount)
    if last_payment < amount:
        print("Your monthly payment = %d and the last payment = %d" % (amount, last_payment))

    else:
        print("Your monthly payment = ", amount)

else:
    print("Option Not Available.")
