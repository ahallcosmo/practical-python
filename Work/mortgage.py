# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month = 0

extra_payment_start_month = 60
extra_payment_end_month = 108
extra_payment = 1000.

while principal > 0:
    month = month + 1
    if(extra_payment_start_month <= month and month <= extra_payment_end_month):
	    monthly_payment = payment + extra_payment
    else:
        monthly_payment = payment
    proposed_balance = principal * (1+rate/12) - monthly_payment
    if(proposed_balance < 0.):
        # This is our last monthly payment
        monthly_payment = proposed_balance + monthly_payment
        proposed_balance = 0.
   
    principal = proposed_balance

    total_paid = total_paid + monthly_payment
    print(month, total_paid, principal)


print('Total paid', total_paid)
print('Months taken', month)