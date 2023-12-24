def factors(n):
    try:
        for j in range(1,n+1):
            if(n%j==0):
                yield j
    except Exception as ex:
        print(ex)

print(list(factors(10)))