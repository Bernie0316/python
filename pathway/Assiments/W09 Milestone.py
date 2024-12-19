"""
File: W08 Milestone.py
Author: Bernie Zhong

Purpose: Writte a Shopping Cart Program code 
"""
# This program inly work for selection 1 and 2
print('Welcome th the Shopping Cart Program!')
print()
print("Please select one of the following:")
# 01 Have menu system that repeats until the user chooses quit.
for stuff in ['1. Add item','2. View cart','3. Remove item','4. Compute total','5. Quit']:
    print(stuff)
select = input('Please enter an action:')
# 02 Create a list that will store the names of the items in the shopping cart.
item = []
add_item = ""
while select != '5':
    # 03 Complete the option to add the name of the item to the list.
    if select.lower() == '1':
        add_item = input("What item would you like to add?")
        print(f"'{add_item.capitalize()}' has been added to the cart.")
        item.append(add_item)
    # 04 Complete the option to display the names of the items in the list.
    elif select.lower() == '2':
        print("The contents of the shopping cart are:")
        for clients in item:
            print(clients)
    elif select.lower() == '3':
        print("Oops! I'm not work on this option yet!")
        print('See u next week')
    elif select.lower() == '4':
        print("Oops! I'm not work on this option yet!")
        print('See u next week')
    else:
        print('Please select a action with number')             
    print()
    print("Please select one of the following:")
    for stuff in ['1. Add item','2. View cart','3. Remove item','4. Compute total','5. Quit']:
        print(stuff)
    select = input('Please enter an action:')
print('Thank you. Goodbye.')
