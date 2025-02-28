


def sum_func (numb1, numb2):
    try:
        return numb1/numb2
    except ZeroDivisionError as e:
            return e

numb1= int(input('enter number the first number '))

numb2 = int (input('enter number the other number'))

print(F"{sum_func(numb1,numb2)}")