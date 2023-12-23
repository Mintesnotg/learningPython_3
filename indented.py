def dups(num1, num2):
    var = []
    numset1 = set({num1})
    numset2 = set({num2})

    for n1 in numset1:
        for n2 in numset2:
            if n1 == n2:
                var += n1

    return var
