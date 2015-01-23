# Problem Set 1.1
# Name: Cole Harris

from math import floor

def findMnthly(balance, mnthRate):
    raw = balance * (mnthRate / (1 - (1 + mnthRate)**(-12)))
    return (floor(raw / 10) * 10 + 10)

def main():
    balance = float(raw_input("Enter the outstanding balance on your credit card: $"))
    intRate = float(raw_input("Enter the annual creadit card interest rate as a decimal: "))

    month = 0
    mnthRate = intRate / 12.0
    mthly = findMnthly(balance, mnthRate)
    
    while balance > 0.0:
        month = month + 1
        balance = (balance * (1 + mnthRate) - mthly)

    print("RESULT")
    print("Monthly payment to pay off debt in 1 year: $" + str(mthly))
    print("Number of months needed: " + str(month))
    print("Balance: $" + str(round(balance, 2)))        
        
main()
