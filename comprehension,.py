def comp_f (n):
    factors= {f :f * f for f in range(1,n+1)}

    return factors

print(comp_f(10))


