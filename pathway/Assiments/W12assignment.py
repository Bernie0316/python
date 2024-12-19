"""
File: W12 assignment.py
Author: Bernie Zhong

Purpose: Writte a Program code 
"""
with open("life-expectancy.csv") as data_information:
    target_year = int(input('Enter the year of interest: '))
    target_max_number = 0.1
    target_min_number = 1000

    max_number = 0.1
    max_year = ""
    max_place = ""
    min_number = 1000
    min_year = ""
    min_place = ""
    total_number = 0

    list_number = []

    for line in data_information:
        parts = line.split(",")
        place = parts[0]
        year = parts[2]
        number = float(parts[3])
        if number > max_number:
            max_number = number
            max_year= year
            max_place = place
        if number < min_number:
            min_number = number
            min_place = place
            min_year= year
        elif int(target_year) == int(year):
            if number > target_max_number:
                target_max_number = number
                target_max_place = place
            elif number < target_min_number:
                target_min_number = number
                target_min_place = place
            list_number.append(number)
    for x in list_number:
        total_number += float(x)
    average = total_number/len(list_number)
    
    print(f"\nThe overall max life expectancy is: {max_number} from {max_place} in {max_year}")             
    print(f"The overall min life expectancy is: {min_number} from {min_place} in {min_year}")
    print()
    print(f'For the year {target_year}:')
    print()
    print(f'The average life expectancy across all countries was {average:.2f}')
    print(f'The max life expectancy was in {target_max_place} with {target_max_number}')
    print(f'The min life expectancy was in {target_min_place} with {target_min_number}')






    