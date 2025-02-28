def allfactors(n):
   
    try:
        for k in range(1,n+1):
         if n % k == 0:
            yield k  
    except Exception  as ex:
       raise  str( ex) 
    
print( f" factors  { set( allfactors(100))}" )


