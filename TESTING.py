def subAdd (x):
    i = 2
    j = x
    while(x - i > 1):
        j*=(x-i)
        i+=2
    print(j)

subAdd(7)