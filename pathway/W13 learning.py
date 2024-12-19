import datetime
print("Test completed")
print(datetime.datetime.now())
print()
for x in range(0,10):
    print(x)
print("tesk completed")
print(datetime.datetime.now()) 
print()   
#############################################
#這招可以讓你每次要印datetime 時打少一點XD
from datetime import datetime
def print_time():
    print("tesk completed")
    print(datetime.now())
    print()
print_time()
for x in range(1,10):
    print(x)
print_time()
############################################################
#######################################################
first_name = input("first_name:")
first_name_initial = first_name[0:1]
last_name = input("last_name:")
last_name_initial = last_name[0:1]
print("Your initials are: " + first_name_initial + last_name_initial)
##########################
def get_initial(name):
    initial = name[0:1].upper()
    return initial

first_name = input("First name: ")
first_name_initial = get_initial(first_name)

last_name = input("last name: ")
last_name_initial = get_initial(last_name)

print("Your initials are: " \
        + first_name_initial \
            + get_initial(last_name))

###############################################################
######################################################################








