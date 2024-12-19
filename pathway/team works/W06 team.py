"""
File: team06.py
Author: Team6

Purpose: Amusement park ride requirements.
"""

age = int(input('What is the age of the first rider?'))
height = int(input('What is the height of the first rider?'))
second = input('Is there a second rider (yes/no)?')

if second.lower() == "no":
    if age >= 18 and height >= 62:
        can_ride = True
        #print('You may have to ride. please be safe and and fun.')
    else:
        can_ride = False
        #print('Sorry, you may not ride.')
elif second.lower() == 'yes':
    age2 = int(input("What's the age of the second rider?"))
    height2 = int(input('What is the height of the second rider?'))
    if height < 36 or height2 <36:
        can_ride = False
    else:
        if age >= 18 or age2 >= 18:
          can_ride = True
        else:
          can_ride = False
if can_ride:
    print('Welcome to the ride. Please be safe and and fun.')
if not can_ride:
    print('Sorry, you may not ride.')
