def multiplication_table(num):
    tens_place = num / 10
    ones_place = num % 10
    first_set = [  (tens_place * i) + (ones_place * i / 10) for i in range(1,11) ]
    second_set = [ (ones_place * i % 10) for i in range(1,11) ]
    for idx, (i, j) in enumerate(zip(first_set, second_set), 1):
        print "%s * %s = %s" % (num, idx, str(i) + str(j))
