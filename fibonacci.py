def fibonacci(n) :
    a,b=0,1
    while (n>0) :
        yield a
        a,b = b, a+b
        n-=1
       
        
    


print(list(fibonacci(10)))

#The combination of automatic packing and unpacking forms a technique known
#as simultaneous assignment,

'''
explicitly assign a series of values to a
series of identifiers
'''