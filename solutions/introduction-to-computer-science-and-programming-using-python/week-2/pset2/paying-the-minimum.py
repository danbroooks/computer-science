
def money(amount):
    amount = round(amount, 2)
    amount = "{0:.2f}".format(amount)
    return '$' + str(amount)

def simulate_year(balance, annualInterestRate, monthlyPaymentRate):
    totalPaid = 0
    interestRate = annualInterestRate / 12.0

    for m in range(12):
        minimumPayment = monthlyPaymentRate * balance
        balance -= minimumPayment
        totalPaid += minimumPayment
        balance += (interestRate * balance)

        print('Month: ' + str(m+1))
        print('Minimum monthly payment: ' + money(minimumPayment))
        print('Remaining balance: ' + money(balance))

    print('')
    print('Total paid: ' + money(totalPaid))
    print('Remaining balance: ' + money(balance))
    print('')
    print('')


# case 1
simulate_year(4213, 0.2, 0.04)

# case 2
simulate_year(4842, 0.2, 0.04)
