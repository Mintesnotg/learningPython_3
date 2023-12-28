def factor(n):
    f=1
    while(f * f<n) :
        if(n %  f==0) :
            yield f
            yield n//f
        f+=1
print(list(factor(10)))