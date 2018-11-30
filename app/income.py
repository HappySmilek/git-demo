import math

def calculate_income(summ, rate, period):

    temp = rate / 1200.

    for i in range(period):
        summ = summ + (summ * temp)

    return round(summ)


summ = 700000
rate = 8
period = 12


