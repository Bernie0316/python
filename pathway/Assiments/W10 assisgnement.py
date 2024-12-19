"""
File: W10 assignment.py
Author: Bernie Zhong

Purpose: Writte a Shopping Cart Program code 
"""
add_item = []
item = None
prices = []
total = 0
print('Welcome to the Shopping Cart Program!\n')
print("Please select one of the following:")
for stuff in ['1. Add item','2. View cart','3. Remove item','4. Compute total','5. Quit']:
    print(stuff)
select = input('Please enter an action:')
while select != '5':
    if select.lower() == '1':
        item = input("What item would you like to add?")
        price = float(input(f"What is the price of '{item}'?"))
        print(f"'{item}' has been added to the cart.")        
        add_item.append(item)
        prices.append(price)  
    elif select.lower() == '2':
        print("The contents of the shopping cart are:")
        for i in range(len(add_item)):
            print(f"{i + 1} {add_item[i]} - ${prices[i]:.2f}")
    elif select.lower() == '3':
        remove = int(input("Which item would you like to remove?"))
        # coz type 1 = 2 in python, so must -1 on type number
        remove  = remove - 1
        add_item.pop(remove)
        prices.pop(remove)
        print(f'{add_item} has been removed.')
        # will print [] with add_item
    elif select.lower() == '4':
        for i in range(len(add_item)):
            total += prices[i]
        print(f"The total price of the items in the shopping cart:\n ${total:.2f}")
        total = 0
    else:
        print('Please select a action with number(from 1 ~ 5)')             
    print()
    print("Please select one of the following:")
    for stuff in ['1. Add item','2. View cart','3. Remove item','4. Compute total','5. Quit']:
        print(stuff)
    select = input('Please enter an action:')
print('Thank you. Goodbye.')

# 12/19 Check: For the selection "4" the old price of item add again when put in now item
# fix: move add_code to selection "4" from selection "1": dosen't work
# fix: remove total price as 0 after "print": Fixd !!!


