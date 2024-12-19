clients = []

new_client = ""
while new_client != "quit":
    new_client = input('What is the name of a client?')
    clients.append(new_client)

for clients in clients:
    print(clients)


# list of Numbers: 
friends = ['Bernie','Lynn']
tips = [11.11,12.12]  

running_total = 0

for tip_amoung in tips:
    running_total += tip_amoung 
    # = running_total = running_total + tip_amoung

print(f'The total is: {running_total:.2f}')



