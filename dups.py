def dups(num1, num2):
   var = []
   numset1 = set({num1})
   numset2 = set({num2})
   
   for n1 in range(len(numset1)):
    for n2 in range(len(numset2)):
       if (numset1[n1] == numset2[n2]):
           var.append(n2)
   return var


print(dups([10,20,30,20],[20,40,10,50]))