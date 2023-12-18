for x in range(1, 10):
    for y in range(1, x + 1):
        print('%sx%s=%s' % (y, x, x * y), end='\t')
    print(" ")
