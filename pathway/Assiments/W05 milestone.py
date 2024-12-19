'''
Author:  Bernie Zhong
File: W05 Assignment.py
Objective: Milestone Adventure Game
'''
answer = input('You are walking through a dark forest and find two items:a MATCH and a FLASHLIGHT. Which one do you want to pick up?')
if answer.lower() == 'match':   
    print('You pick up the match and strike it, and for an instant, the forest around you is illuminated. You see a large grizzly bear, and then the match burns out. Do you want to RUN, or HIDE behind a tree?')
#else必須跟if同等級/else are the same posititon(level) with if.
    tool = input()
#try02 : link 'answer' with input(answer2) were works
    if tool.lower() == 'run':
        print("You run away from bear, and dear runs after")
    else:
        print('You hide behide the tree')
else:
    print('You pick up the flashlight and turn it on. You see the pathway lit up in front of you, but you thought you also heard something off to the side. Do you want to FOLLOW the path or LOOK in the trees for the thing that made the noise?')
    answer2 = input()
    if answer2.lower() == 'follow':
        print('You followed the path, and ')
    #try03 : 'print' will link to the match position 'if'.    
    else:
        print("You look in the trees and find there has a hole on the tree. The voice you heard is from this hole. Do you want 'WALK' in to the hole or 'GREETING' to the hole? ")  
        look = input()
        if look.lower() == 'walk':
            print('')
        else:
            print('')    
          
#try01 : both the 大小寫 works. welldone.

