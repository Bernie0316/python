# 除了"while" 還有另一種loop 叫做 'for'


for name in ['Bernie','Zhong']:
    print(name)

for index in range(0,2):
    print(index)

names = ['Lynn','Hu']
index = 0
while index < len(names):
    # 'len' 是甚麼?
    print(names[index])
    # change the condition
    index = index + 1


items = ["haha","ydk","誰啦"]

for items in items: 
    print(f'the item is: {items}')


people = ['Bernie','Zhong']
print()
#for loop
for idk in people:
    print(idk)
index = 0
#while loop
while index < len(people):
    print(people[index])
    index = index + 1
print()

word = 'you'
y = word[0]
o = word[1]
u = word[2]
print(f'{o}--')
#for o in secret_word:
#    print(f'-{o}-')
