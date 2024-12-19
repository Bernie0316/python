"""
File: W11 milestone.py
Author: Bernie Zhong

Purpose: Writte a  Program code 
"""
max = 0.1

with open("life-expectancy.csv") as life_expectancy:
    # Entity,Code,Year,Life expectancy
    # Afghanistan,AFG,1950,27.638
    next(life_expectancy)
    for line in life_expectancy:
        parts = line.split(",")
        expectancy = float(parts[3])
        if expectancy > max:
            max = expectancy
    print(max)
        