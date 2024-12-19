#<=這個符號打在code裡的話不會印出任何東西，所以可以拿來當作筆記XD
first_name='Bernie'
last_name='Zhong'
print(first_name+last_name)
#若要印出空格，只能被算在''裡
#like: print('(我是空白建)')
print('Hello '+ first_name+' '+last_name)
print('============我是分隔線==============')
#接下來是大小寫列出方法(除了在code裡打出大小寫之外)
sentence='the dog is named Sammy'
#以下為全部大寫
print(sentence.upper())
#以下為全部小寫
print(sentence.lower())
#以下為句首大寫
print(sentence.capitalize())
#以下為字首大寫
print(sentence.title())
#我還不知道為啥這結果v會是(2)....
print(sentence.count('a'))
print('============我是分隔線==============')
first_name=input('What is your first name?')
last_name=input('What is your last name?')
print('Hello '+first_name.capitalize()+' '+ last_name.capitalize())
#這裡就試試看"句子"代表可以隨便到什麼程度XD
sth='i love you'
print(sth.title())
