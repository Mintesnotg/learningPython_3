def is_multiple ( n ,m ):
   return (n %m==0)

def Is_Even (n):

   lbs= n & 1

   return lbs

def custommax(data):
   
   ln=len(data)-1
   max_value=data[ln]
   while(ln>=0):
      if(max_value < data[ln-1]):
         max_value=data[ln-1]

   
      ln+=-1   
   
   
   
   return max_value


def custonmmin(data):
   
   min_value = max_value = data[0]

   ln=len(data)-1
   min_value=data[ln]
   while(ln>=0):
      if(min_value > data[ln-1]):
         min_value=data[ln-1] 
      elif (max_value < data[ln-1]):
         max_value=data[ln-1]
         
      ln+=-1   

   
   
   return (min_value,max_value)
 



#  return (  custonmmin(data),  custommax( max_value))

values=(custonmmin([12,23,3,9,32,90]))

print(F" is multiple {is_multiple(4,2)} ")
print( Is_Even(43))

print(F" min and max values {values} ")




