 
my_guests ={}

my_guests['Alice']=(28,'alice@email.com')
my_guests['Bob']=(28,'bob@email.com')
my_guests['Charlie']=(35,'charlie@email.com')
print(my_guests)

my_guests['David']=(22,'david@email.com')

del my_guests ['Bob']

print(my_guests)




def get_guest_info(guest_name:str):
        if(guest_name in my_guests):
            return F"{guest_name} (Age: {my_guests[guest_name][0]}) is coming to the party! Email: {my_guests[guest_name][1]}"
        else: 
            return F"{guest_name} is not on the guest list."
        
print(F" total number of guests is {len(my_guests)     }") 
print( get_guest_info("David"))


guestcoll= list()



def display_guests_orderbyage():
     
     for index,key in enumerate( my_guests):
          print(my_guests[key])
          yield my_guests[key]


allgusts=list( display_guests_orderbyage())
print( F" all guests descending age {sorted(allgusts,key=lambda x:x[0],reverse=True)}" )
print( F" all guests ascending age {sorted(allgusts,key=lambda x:x[0],reverse=False)}" )



     

