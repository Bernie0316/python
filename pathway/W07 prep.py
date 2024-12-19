#Loop迴圈應用
tip = float(input("what's the amount?"))
if tip<0:
    print('Sorry the tip can not be nagative')
    tip = float(input("what's the amount?"))
    #if只會出現一次
print(f'You have an amount of ${tip:.2f}')
#loops:迴圈
while tip<0:
    print('Sorry the tip can not be nagative')
    tip = float(input("what's the amount?"))
    #會回到第7行(永遠)     
print(f'You have an amount of ${tip:.2f}')

#loop迴圈_模塊
''''''
answer = "answer"
anwser = float(input("What's the answer?"))
while anwser != 'answer':
    print('This is not the answer')
    anwser = float(input("What's the answer?"))
print("this's the answer")
''''''