def max(a,b,c):
    if (a >= b) and (a >= c):
        largest = a

    elif (b >= a) and (b >= c):
        largest = b
    else:
        largest = c

    return largest
print(max(a=10,b=50,c=70))

