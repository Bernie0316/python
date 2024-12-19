"""
File: W08 Milestone.py
Author: Bernie Zhong

Purpose: Writte a Wordle game code 
"""
secret = "secret"
secret_len = len(secret)
times = 1
hints_len = " _" * len(secret)
print(f"Your hints is:{hints_len}")
guess = input('What is your guess?')
guess_len = len(guess)

while guess.lower() != secret.lower():
    if guess_len == secret_len:
        for i,letter in enumerate(guess):
            if letter.lower() == secret[i]:
                print(letter.upper(), end = "")
            elif letter.lower() in secret:
                print(letter.lower(), end = "")
            else:
                print(" _", end = "")
    else:
        print('The letter must be same with secret word.')
    guess = input('\nWhat is your guess?')
    guess_len = len(guess)
    times = times + 1
print('Congradulations! You guess it!')
print(f'it took you {times} guess')

