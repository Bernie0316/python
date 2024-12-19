grade = int(input('What is your grade?'))
if grade >= 90:
    letter = "A"        
elif grade >= 80:
    letter = 'B'
elif grade >= 70:
    letter = 'C'
elif grade >= 60:
    letter = 'D'
else:
    letter = 'F'
print(f'Your letter grade is {letter}')
print()
if grade >= 70:
    print('Congratulations!!\nYou pass the class!!!')
else:
    print('See you the next semester. \nKeep study hard.')
