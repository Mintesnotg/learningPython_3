def whileloop(x):
    reversed= str()

    len=x.__len__()
    while(len>0):
        len=len-1
        reversed+=x[len]

    return reversed

print(f'-while loop- {whileloop("Mintesnot")}')


def forloop(iter):
    onlyevens=0
    for it in iter:
        if(it%2==0):
            onlyevens+=it

    return onlyevens
    

print( f" -- for loop {forloop([10,1,3,2,4,9])}" )

## range 

def inrange (values):
    indexes = []

    for i in range(len(values)):
        if(i%2==0):
         yield i
        else : continue
    return indexes

print(inrange([100,1,2,3]))


def cont_(values):
    var= []
    for i in range(len(values)):

        if(values[i]<0) :
            continue
        else : yield values[i]
    print("-- changing list--")
    var=[]
    return var

print(cont_([10,-1,90,-3,-12,100]))


def break_(s):
    brk=[]

    for val in s:
        if(val<0):
         break
        else : yield val
    
    return brk

print(break_([10,1,8,-10,2,3]))


    

    





                  
             
        






