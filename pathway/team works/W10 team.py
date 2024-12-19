names = []
balance = []

print("Enter the names and balances of bank accounts (type: quit when done)")

account_names = None
account_balance = None

while account_names != "quit":
    account_names = input("What is the name of this account?")
    if account_names != "quit":
        names.append(account_names)
        account_balance = float(input("What is the balance?"))        
        balance.append(account_balance)
print()
print('Account Information:')
total = 0
for i in range(len(names)):
    name = names[i]
    balances = balance[i]
    print(f"{i + 1}.{name} - ${balances:.2f}")
    total += balances
    highest_balance = max(balances)
    position = names.index(highest_balance)
print()    
print(f"total:${total:.2f}")
average = total / len(names)
print(f"average:${average:.2f}")
print(f"highest balance:{names[position]} - ${highest_balance}") 
print()
yes_or_no = input("Do you want to update an account?")
update = float(input("What account index do you want to update?")) 
new_amount = float(input("What is new amount?"))
print()

print('Account Information:')
print()







