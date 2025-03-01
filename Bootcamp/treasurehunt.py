

rows = int (input("Enter nummber of rows"))
cols = int (input("Enter number of columons"))
trow= int(input( F" Choose a row between  {rows} - {cols} to hide the treasure" ))
tcol =int( input( F" Choose a columon between  {rows} - {cols} to hide the trasure   "))

while (trow > rows or tcol > cols):
    if(trow > rows):
        trow= int(input( F" invalid {trow} please enter a columon  {rows} - {cols} " ))
    elif(tcol > cols):
        tcol =int( input( F" invalid {tcol} please enter a columon  {rows} - {cols}   "))
    else :
        trow= int(input( F" invalid {trow} please enter a columon  {rows} - {cols} " ))
        tcol =int( input( F" invalid {tcol} please enter a columon  {rows} - {cols}   "))


for r in range(rows):

    for col in range(cols):

        if(not(trow == r and tcol == col)):
            print("*", end= " ")
        else :
             print ("T", end= " ")
    print()

          
  