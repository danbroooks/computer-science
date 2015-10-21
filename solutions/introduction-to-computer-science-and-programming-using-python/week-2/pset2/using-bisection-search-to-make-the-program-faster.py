
import math

def money(amount):
    amount = round(amount, 2)
    amount = "{0:.2f}".format(amount)
    return '$' + str(amount)

def compound(sum, rate, power):
    for i in range(power):
        sum *= 1 + rate

    return sum

def simulate_year(startBalance, annualInterestRate):
    interestRate = annualInterestRate / 12.0
    low = startBalance / 12.0
    high = compound(startBalance, interestRate, 12)

    epsilon = 0.1

    while (True):
        payment = round(low + ((high - low) / 2), 2)

        balance = startBalance
        for m in range(12):
            balance -= payment
            balance += (interestRate * balance)

        if (abs(balance) < epsilon):
            break

        print(str(balance))

        if (balance > 0):
            low = payment
        else:
            high = payment

    print('Lowest Payment: ' + money(payment))
    print('')


# case 1
simulate_year(320000, 0.2)

# case 2
simulate_year(999999, 0.18)
