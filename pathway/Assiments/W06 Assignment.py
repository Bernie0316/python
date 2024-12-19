'''
Author:  Bernie Zhong
File: W06 Assignment.py
Objective: Adventure Game
'''
answer = input('You are walking through a dark forest and find two items:\na MATCH and a FLASHLIGHT.\nWhich one do you want to pick up?')
if answer.lower() == 'match':   
    match = input('You pick up the match and strike it, and for an instant, the forest around you is illuminated.\nYou see a large grizzly bear, and then the match burns out. \nDo you want to RUN, or HIDE behind a tree?')
    if match.lower() == 'run':
        run = input("You run away from bear, and dear follows behind you. Will you GIVE UP let the bear eats you or CRY for help?")
        if run.lower() == 'give up':
            #END
            print('The bear eats you. GAME OVER')
        else:
            #END
            print('You cried for help. Suddently, you fund your match become a boom to attack the bear. And the bear were explode away by the match-boom. You survived !!!')    
    elif match.lower() == 'cry':
        hide = input('You hide behide the tree, and you can still hear it try to walks around here to find you. Do you want CLIMB on tree or FIGHT with the bear ?')
        if hide.lower() == 'climb':
            #END
            print('')
        else:
            #END
            print('') 
    else:
        print('')           
elif answer.lower() == 'flashlight':
    flashlight = input('You pick up the flashlight and turn it on. You see the pathway lit up in front of you, but you thought you also heard something off to the side. Do you want to FOLLOW the path or LOOK in the trees for the thing that made the noise?')
    if flashlight.lower() == 'follow':
        follow = input('You followed the path, and you see a house in frout of you. Will you PASS or GET inside the house?')
        if follow.lower() == 'pass':
            #END
            print('')
        else:
            #END
            print('')    
    elif flashlight.lower == 'look':
        look = input("You look in the trees and find there has a hole on the tree. The voice you heard is from this hole. Do you want 'WALK' in to the hole or 'GREET' to the hole? ")  
        if look.lower() == 'walk':
            #END
            print('')
        else:
            #END
            print('')    
    else:
        print('')        
#here's a surprise
else:
    print("You keep walking through the forest but it's too dark that you can's see so you try to open your eyes again. Then you fund that you are lie on your bed. It just a dream....")                        

          

