def multipleoftwo_three (n):

    while(n >0):

        if(n %2==0):
            yield n
        if(n % 5==0):
            yield n
        n-=1
print(set(multipleoftwo_three(15)))



