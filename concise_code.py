import math

import random

def compcondition(n):

    x = True if(n %2==0) else False

    return x


print(compcondition(10))


def randomization (a,current,b,n):
    next = (a*current + b) % n
    var= random.randrange(2,100,1)
    return var

print(randomization(1,2,3,40))



# squares = [k * k for k in range(1, n+1)]

