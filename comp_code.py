def comp_code (n):

    factors =[ f for f in range(1,n+1) if n % f==0]
    return sum(factors)
print(comp_code(10))

def squares(n):

    sqrs= sum( {s*s for s in range (1,n+1) })

    return sqrs
print(squares(10))