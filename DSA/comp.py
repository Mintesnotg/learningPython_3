
import random


def randomization (a,current,b,n):
    next = (a*current + b) % n
    var= random.randrange(2,100,1)
    return var

print(randomization(1,2,3,40))