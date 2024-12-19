"""
File: team11.py
Author: Team6

Purpose: Split the name and title.
"""
with open("hr_system.txt") as hr:
    hr = open("hr_system.txt")
    for line in hr:
        names = line.split(" ")
        name = names [0]
        title = names [2]         
        print(f"Name: {name}, Title:{title}")
        
        

