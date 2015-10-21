
import math

def money(amount):
    amount = round(amount, 2)
    amount = "{0:.2f}".format(amount)
    return '$' + str(amount)

def simulate_year(startBalance, annualInterestRate):
    interestRate = annualInterestRate / 12.0
    low = 0
    high = startBalance / 6

    epsilon = 0.01

    while (True):
        payment = low + ((high - low) / 2)

        balance = startBalance
        for m in range(12):
            balance -= payment
            balance += (interestRate * balance)

        if (abs(balance) < epsilon):
            break

        if (balance > 0):
            low = payment
        else:
            high = payment

    payment = math.ceil(payment / 10) * 10
    print('Lowest Payment: ' + money(payment))
    print('')


# case 1
simulate_year(3329, 0.2)

# case 2
simulate_year(4773, 0.2)

# case 3
simulate_year(3926, 0.2)
