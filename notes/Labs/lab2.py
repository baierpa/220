rate_input = input('enter the annual interest rate: ')
rate = eval(rate_input)
days_input = input('enter the number of days in the billing cycle: ')
days = eval(days_input)
previous_balance_input = input('enter the previous net balance: ')
previous_balance = eval(previous_balance_input)
payment_input = input('enter the payment amount: ')
payment = eval(payment_input)
payment_day_input = input('enter the day the payment was made: ')
payment_day = eval(payment_day_input)

balance_days = previous_balance * days
payment_days = payment * (days - payment_day)
balance_payment = balance_days - payment_days
balance_payment_days = balance_payment / days

monthly_interest_rate = rate / 1200
monthly_interest = balance_payment_days * monthly_interest_rate
print(monthly_interest)