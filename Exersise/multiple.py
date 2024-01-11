def is_multiple ( n ,m ):
   x = True if(n %m==0) else False
   return x


def isEven(n):

 lsb= n & 1
 return lsb



print( is_multiple(4,2))
print( isEven(21))