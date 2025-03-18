

def sum_of_the_squares(n:int):
    sumval=0

    for i in range(n):

        sumval+=i*i
    
    return sumval


print( sum_of_the_squares(5))


def sum_of_odd_square ( n : int):

    return sum(num * num for num in range(n))


print(F" odd square {sum_of_odd_square(5)}") 
    