# Problem Set 1.1
# Name: Cole Harris

import math

def main():
    initBalance = float(raw_input("Enter the outstanding balance on your credit card: $"))
    yearlyRate = float(raw_input("Enter the annual creadit card interest rate as a decimal: "))

    monthRate = (yearlyRate / 12.0)

    Bounds = [(initBalance / 12.0), ((initBalance * (1 + monthRate) ** 12) /  12)]
    monthTry = ((Bounds[1] - Bounds[0]) / 2 + Bounds[0])

    attempts = 0
    
    while (Bounds[1] - Bounds[0]) > 0.005:
        month = 0
        balance = initBalance
        
        monthTry = (Bounds[0] + Bounds[1]) / 2
        
        attempts = attempts + 1
        
        #print("Trying " + str(Bounds) + " or " + str(monthTry))
        #if raw_input("Continue Y/N ?") == "N":
        #    break
        
        while month < 12:
            month = month + 1
            balance = (balance * (1 + monthRate) - monthTry)
        #    print("\tCheck Month "+ str(month) + " at $" + str(balance) + "")
            if balance < 0:
                break

        if balance == 0.0:
            break
        elif balance > 0.0:
            Bounds[0] = monthTry
        else:
            Bounds[1] = monthTry


    print("RESULT")
    print("Monthly payment to pay off debt in 1 year: $" + str(round(monthTry,2)))
    print("Number of months needed: " + str(month))
    print("Balance: $" + str(round(balance, 2)))
    print("\n\tIt took %i attempts!" % attempts)

main()
