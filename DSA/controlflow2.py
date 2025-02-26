def controlflow(numb):
    if(numb>10):
        
        return f"{numb } is above 10 "
    elif (numb==10):
        return f"{numb} is equals 10"
    elif (numb<10):
        return f"{numb} is less than 10"
    else :
        return f"{numb} is unknown"



print(controlflow(11))
