def unpacking(n):

    return ( n // 2 , n * n)
x,y= unpacking(10)
print(x)
print(y)

def unpacking2():

    for x,y in [(7,2),(10,20),(90,100)]:
        yield x
        yield y
print(list(unpacking2()))