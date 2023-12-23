def controlflowinpy(numb):
    if(numb.__len__()<=5):
        return f"{numb} is small string"
    elif(numb.__len__()>=5):
        return f" {numb} is long string"
    elif (numb.__len__()==0):
        return f" {numb} is empty"
    else: return numb


print(f'{controlflowinpy("Mintesnot")}' )

def  controlflow2(x):
    if(x>70 and x<80):
        return f" {x} is avarage result "
    elif(x> 80 and x<90):
        return f"  {x} is good result "
    elif (x >90 and x<= 100):
        return f" {x} is excellent result "
    else :
        return  f" {x} is poor result "
print(f"{controlflow2(10)}")
