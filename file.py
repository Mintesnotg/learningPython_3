def Writetofile(lns) :
        try:
            wr=open("C:/Users/Moon/Desktop/Witi_rng_from_py.txt","r")
            for ln in lns:
                 wr.writelines(ln)
        except Exception as ex :
           return print( ex)

        print("finshed writing to file..")

                 

fl=open("C:/Users/Moon/Desktop/Message_Cannot.txt","r")
lines=fl.readlines()

print(Writetofile(lines))