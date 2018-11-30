def calculate_cashback(summ, type_of_operation):
    cashback = 0.
    if type_of_operation == 'vip':
        cashback = summ * 0.3
    elif type_of_operation == 'hight':
        cashback = summ * 0.05
    else:
        cashback = summ * 0.01

    if cashback > 3000:
        cashback = 3000.

    return cashback

# summ = 0
#print( 'original purchase =', test_calculate_cashback( 1000, 'original'))
#print( 'vip =', test_calculate_cashback( 1000, 'vip') )
#print( 'hight =', test_calculate_cashback( 1000, 'hight'))
#print( '>100000 =', test_calculate_cashback( 100000, 'vip'))
