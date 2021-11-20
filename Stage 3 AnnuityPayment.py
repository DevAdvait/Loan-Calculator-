import math
print("""What do you want to calculate?
type "n" for number of monthly payments,
type "a" for annuity monthly payment amount,
type "p" for loan principal:""")

mode = str(input())

if mode == "n" or mode == "N":
    #Taking inputs
    principal = abs(int(input("Enter the loan principal: ")))
    monthly_payment = abs(int(input("Enter the monthly payment: ")))
    interest = round(float(input("Enter the loan interest: ")), 2)

    #Calculating nominal (monthly) interest
    i = (interest / 100) / 12 * 1

    #Calculating Number of months
    var = abs(monthly_payment / (monthly_payment - i * principal))
    n = abs(round(math.log(var, (1 + i)), 2))

    #Converting floating to higher integer
    months = -(-n // 1)

    #Converting months to Years and Months
    years = months / 12
    rem_months = months % 12

    #Printing Total Time
    if years == 1:
        print("It will take 1 year to repay this loan!")
    elif years < 2:
        print("It will take 1 year and %d months to repay this loan!" % rem_months)
    elif months % 12 == 0:
        print("It will take %d years to repay this loan!" % years)
    else:
        print("It will take %d years and %d months to repay this loan!" % (years, rem_months))

elif mode == "a" or mode == "A":
    principal = abs(int(input("Enter the loan principal: ")))
    n = abs(int(input("Enter the number of periods: ")))
    interest = round(float(input("Enter the loan interest: ")), 2)

    i = (interest / 100) / 12 * 1

    num = i * math.pow((1 + i), n)
    de_num = math.pow((1 + i), n) - 1

    ann = principal * (num / de_num)

    b = abs(-(-ann // 1))
    print("Your monthly payment = %d!" % b)


elif mode == "p"  or mode =="P":
    ann = abs(float(input("Enter the annuity payment: ")))
    n = abs(int(input("Enter the number of periods: ")))
    interest = round(float(input("Enter the loan interest: ")), 2)

    i = (interest / 100) / 12 * 1

    de_num = (i * (math.pow((1 + i), n))) / (math.pow((1 + i), n) - 1)

    p = ann / de_num

    print("Your loan principal = %d!" % p)

else:
    print("Enter a correct option.")