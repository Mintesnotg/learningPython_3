
guests= list ()

# custom_guest= str (input("Enter your guest Name"))
# to_be_remove_guest=str (input("Enter your guest you want to remove"))

def addtolist(custom_guest):
    guests.append(custom_guest)
    print(F"you have successfully added {custom_guest} to your list")

def  removefromlist(to_be_remove_guest):
    if(to_be_remove_guest not in guests):

        print(F" guest {to_be_remove_guest} is not your list")
    else:
        guests.remove(to_be_remove_guest)
        print(F"you have successfully removed {to_be_remove_guest} from your list")
    



def check_whoonnlist():
    for guest in guests:
        print(guest) 

def perform_action(action_numb):
    
    match(action_numb):
        case 1:
           stri= str( input("Enter your gust name"))
           addtolist(stri)
           
        case 2:
            stri= str( input("Enter your gust name to be removed"))
            removefromlist(stri)
            
        case 3:
            check_whoonnlist()
            
        case _:
            print("Invalid action. Please choose a valid option.")
            




while (True):
    action_numb = int(input("what actioin you want to perform \n 1.to add guest to your list \n 2. reomve guest to your list \n 3. see who is in your guest list \n"))

    if action_numb not in [1, 2, 3]:  #  Corrected condition
        
        print("Invalid choice. Exiting program.")

        break  

    perform_action(action_numb)       



# while True :

#     int( input("Enter 1 to add guest to your list"))
#     int( input("Enter 2 to reomve guest to your list"))
#     int( input("Enter 3 to see who is in your guest list"))






