def customsqrt():
        try:
            val=0
            count=0
            while val >=0:
                val=int(input('Enter a postive digit :'))
                if val<=0:
                    print("your digit must be postive")
                    return 
                else :   count+=val; continue
        except (ValueError,EOFError) as  ex:
             return print(f"exeption is {ex}")
        finally  :
             print(f"sum of the entered numbers is {count}")
    
customsqrt()


        
           





