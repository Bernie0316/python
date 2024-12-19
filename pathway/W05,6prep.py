#if...then,else 應用
country = input('Enter the name of your country: ')
if country == 'canada':
    print('So you must like hockey!')
else:
    print('You are not from Canada')            
#這邊會print第二種結果
#如果要print 出第一種結果，要這樣
#if country.lower() ==
#可達成無視大小寫print第一種結果    
#=====================================
price = input('how much did you pay? ')
price = float(price)
if price >= 1.00:
    tax = .07
else:
    tax = 0
print('Tax rate is: '+str(tax))
#比大小符號解釋:
#<:小於
#>:大於
#<=:小於等於
#>=:大於等於
#!=:不等於
#======================================
''''''
province = input('What province do you live in?')
tax = 0
if province == 'Alberta':
    tax = 0.05
if province == 'Nunavut':
    tax = 0.05
if province == 'Ontario':
    tax = 0.13
else:
    tax = 0.15    
print(tax)
''''''
#if...else順序:If(a,b),else(a,b)(下一頁)
#如果if(a)過可以接if(b)但不可接else(b)，如果if(a)沒過跳else

#第一種:
gpa = float(input("What was your grade point average?"))
lowest_grade = float(input('What was your lowest grade?'))
#第二種:
#lowest_grade = input("What's your lowest grade?")
#lowest_grade = float(lowest_grade)
#第一種:
if gpa >= .85:
  if lowest_grade >= .70:
#第二種:      
#if gpa >= .85 and lowest_grade >= .70:
    honour_roll = True 
else:
    honour_roll = False
if honour_roll:    
    print('you made the honour roll')

#==================================================

is_hot = True
#如果打'false' 會印出"it's not hot"
#1_is
if is_hot:
    print("it's hot")
#2_is
if is_hot == True:
    print("it's hot") 
#=============================
if not is_hot:
    print("it's not hot")

if is_hot == False:
    print("it's not hot")         



