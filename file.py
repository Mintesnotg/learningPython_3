def Writetofile(lns) :
        wr=open("C:/Users/Moon/Desktop/Witing_from_py.txt","w+t")
        for ln in lns:
         wr.writelines(ln)
         
print("finshed writing to file..")

fl=open("C:/Users/Moon/Desktop/Message_Cannot.txt","r")

lines=fl.readlines()

Writetofile(lines)






   # print(ln)
