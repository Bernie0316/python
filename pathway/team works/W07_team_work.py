'''
File: team07.py
Author: Team7

Purpose: Guess my number game.

'''
import random

magic_number = random.randint(1,10)
#magic_number = float(input("What's the magic number?"))
guess = float(input("What's your guess?"))


while guess != magic_number:
   guess = float(input("What's your guess?"))
   if guess > magic_number:
      print('lower')
   elif guess < magic_number:
      print('higher')
else:
   print('You guessed it!')
  
      
   

  

   


#while magic_number > "6":
#    print('lower')
#    anwser = float(input("What's the magic number?"))
#while magic_number < "6":
#    print('higher')
#    anwser = float(input("What's the magic number?"))
