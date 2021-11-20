import argparse
import math

parser = argparse.ArgumentParser()
parser.add_argument("--type", type=str, required=False, choices=["annuity", "diff"], help="")
parser.add_argument("--principal", type=int, required=False, help="")
parser.add_argument("--periods", type=int, required=False, help="")
parser.add_argument("--interest", type=float, required=False, help="")
parser.add_argument("--payment", type=int, required=False, help="")

args = vars(parser.parse_args())
"""
Assigning args to variables
"""
type_payment = args["type"]
pri_pal = args["principal"]
interest = args["interest"]
m_amount = args["payment"]
month = args["periods"]
"""
Check whether:
All necessary parameters are entered
"""
if (type_payment is None) or (type_payment == "diff" and m_amount is not None) or \
        (interest is None) or (month is not None and month < 0):
    print("Incorrect parameters")
else:
    i = interest / (12 * 100)
    if type_payment == "diff":
        # assign principal to overpayment
        overpayment = pri_pal
        # looping for numbers of months
        for x in range(1, month + 1):
            # calculating differentiated payments
            d_num = math.ceil(pri_pal/month + i * (pri_pal - pri_pal*(x - 1)/month))
            #deducting each payment from principal to get total overpayment amount
            overpayment -= d_num
            print(f"Month {month}: payment is {d_num}")
        print(f"\nOverpayment = {abs(overpayment)}")

    elif type_payment == "annuity":
        #condition to find total months needed to pay loan
        if month is None:
            month = math.ceil(math.log(m_amount / (m_amount - i * pri_pal), 1 + i))
            years = month // 12
            months = month % 12
            if months == 0:
                print(f"It will take {years} to repay this loan!")
            else:
                print(f"It will take {years} years and {months} to repay this loan!")
        #find principal
        elif pri_pal is None:
            pri_pal = math.floor(m_amount / (i / (1 - 1 / math.pow(1 + i, month))))
            print(f"Your credit principal = {pri_pal}!")
        #find monthly payment
        else:
            m_amount = math.ceil(pri_pal * i / (1 - 1 / math.pow(1 + i, month)))
            print(f"Your annuity payment = {m_amount}!")
        overpayment = month * m_amount - pri_pal
        print(f"Overpayment = {overpayment}")














