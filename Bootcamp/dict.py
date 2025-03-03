 
my_dict ={}

my_dict['Alice']=(28,'alice@email.com')
my_dict['Bob']=(28,'bob@email.com')
my_dict['Charlie']=(35,'charlie@email.com')
print(my_dict)

my_dict['David']=(22,'david@email.com')

del my_dict ['Bob']

print(my_dict)




def get_guest_info(guest_name:str):
        if(guest_name in my_dict):
            return F"{guest_name} (Age: {my_dict[guest_name][0]}) is coming to the party! Email: {my_dict[guest_name][1]}"
        else: 
            return F"{guest_name} is not on the guest list."
print( get_guest_info("David"))
for index,value in enumerate( my_dict):
     print(index)


