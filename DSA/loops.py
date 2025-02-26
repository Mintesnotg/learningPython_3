
def my_whileloop (string):
    reverse=str()
    len=string.__len__()-1
    while (len>=0):
     reverse+=string[len]
    #  print(string[len])
     len-=1
    return reverse

mylist =[10,20,30,40]
def  my_forloop(mylist):
    totalamount=int()
    # len=string.__len__()-1
    for index in range( len( mylist)):
        if(mylist[index]==30):
           break
        totalamount+=mylist[index]
    return totalamount
    
      





print( my_forloop(mylist))
