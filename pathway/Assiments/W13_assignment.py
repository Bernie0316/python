"""
File: W13 assignment.py
Author: Bernie Zhong

Purpose: Writte a Wind Chill Calculation Program code 
"""
import math

# With while loop:
wind_speed = 5
# calculation for F  
def wind_chill_F(wind_speed, temperature):
    v = wind_speed
    t = temperature
    return 35.74 + 0.6215*t + (0.4275*t - 35.75) * (v ** 0.16)
# calculation for C  
def wind_chill_C(wind_speed, temperature):
    v = wind_speed 
    t = temperature * 9 / 5 + 32
    return 35.74 + 0.6215*t + (0.4275*t - 35.75) * (v ** 0.1
print("Welcome to the Wind Chill Calculation program !")
temperature = float(input("\nWhat is the temperature? "))
t = temperature * 9 / 5 + 32
unit = input("Fahrenheit or Celsius (F/C)? ")
print()
while wind_speed <= 60:
    if unit.lower() == "f":
        print(f"At temperature {temperature}F, and wind speed {wind_speed} mph, the windchill is: {wind_chill_F(wind_speed, temperature):.2f}F")    
        wind_speed += 5        
    elif unit.lower() == 'c':     
        print(f"At temperature {t}F, and wind speed {wind_speed} mph, the windchill is: {wind_chill_C(wind_speed, temperature):.2f}F")   
        wind_speed += 5
    else: 
        print("Please inter correct unit of temerature (C/F). \n")     
print("\nLet's do for loops!")

# With for loops:
wind_speed = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60]
temperature = float(input("\nWhat is the temperature? "))
print("Welcome to the Wind Chill Calculation program !")
unit = input("Fahrenheit or Celsius (F/C)? ")
print()
for num in wind_speed:
    wind_speed = num
    def wind_chill_F(wind_speed, temperature):
        v = wind_speed
        t = temperature
        return 35.74 + 0.6215*t + (0.4275*t - 35.75) * (v ** 0.16)
    # calculation for C  
    def wind_chill_C(wind_speed, temperature):
        v = wind_speed 
        t = temperature * 9 / 5 + 32
        return 35.74 + 0.6215*t + (0.4275*t - 35.75) * (v ** 0.16)
    t = temperature * 9 / 5 + 32
    if unit.lower() == "f":
        print(f"At temperature {temperature}F, and wind speed {wind_speed} mph, the windchill is: {wind_chill_F(wind_speed, temperature):.2f}F")           
    elif unit.lower() == 'c':     
        print(f"At temperature {t}F, and wind speed {wind_speed} mph, the windchill is: {wind_chill_C(wind_speed, temperature):.2f}F")   
    else: 
        print("Please inter correct unit of temerature (C/F). \n")     
print("\nThank you, Good bye !")




