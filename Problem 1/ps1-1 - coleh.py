# Problem Set 1.1
# Name: Cole Harris

def minMonthly(minPayRate):
    """Returns minimum monthly payment rate * ? (usually Balance)."""
    return lambda x: x * float(minPayRate)

def interestPaid(annualInterestRate):
    """Returns Interest Paid given Annual Interest Rate & Balance."""
    return lambda x: x / 12.0 * float(annualInterestRate)

def principalPaid(minMonthlyPay,interestPay):
    """Calculate how much principal is paid."""
    return minMonthlyPay - interestPay

def balanceToDate(principal,balance):
    """Calculate running balance - principal per month."""
    return float(balance) - float(principal)
    return b2d

def main():
    balance = float(raw_input("Enter the outstanding balance on your credit card: $"))
    intPay = interestPaid(raw_input("Enter the annual creadit rate as a decimal: "))
    minMth = minMonthly(raw_input("Enter the minimum monthly payment rate as a decimal: "))
    month = 0
    totalPaid = 0
    
    while month < 12:
        month = month + 1

        minM = round(minMth(balance), 2)
        intP = round(intPay(balance), 2)
        prnP = principalPaid(minM,intP)
        totalPaid = totalPaid + minM
        balance = balanceToDate(prnP,balance)
        
        print("Month: " + str(month))
        print("Minimum monthly payment: $" + str(minM))
        print("Principal Paid: $" + str(prnP))
        print("Remaing Balance: $" + str(balance))

    print("RESULT")
    print("Total amount paid: $" + str(totalPaid))
    print("Remaining balance: $" + str(balance))


        
        
main()
