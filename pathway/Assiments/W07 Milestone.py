"""
File: W07 Milestone.py
Author: Bernie Zhong

Purpose: Writte a Wordle game code 
"""
#01 The secret word
secret_word = 'word'

#give the time of guess(start)
guess_count = 0
# + 1 every time
guess_count += 1

#02 The promption of geussing
print('Welcome to the wrod guessing game!')
guess = input("What is your guess?")

#03 continue looping for incorrect
while guess.lower() != secret_word:
    print('Your guess is not correct')
    guess = input("What is your guess?")
    # + 1 time every when "while" shows again
    guess_count += 1


    
print("Congratulations! You guessed it!")

#Claculation of the times of guessing
print(f'It took you {guess_count} guess')


#10/25: the count shown "0" trying to find way isn't count.
#'.count' doesn't work for counting time of 'while'

#10/29: 定義times of guess by 'name = 0'
#'name = name + 1' in every shows up. 
