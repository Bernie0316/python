# first number is the width of the tire in millimeters. 
# The second number is the aspect ratio. 
# The third number is the diameter in inches of the wheel that the tire fits.
# The volume of space inside a tire can be approximated with this formula:
import math

print("> python tire_volume.py")

def volume(width,aspect,diameter):
    w = width
    a = aspect
    d = diameter
    return (math.pi * (w * w) * (a * (w*a + 2540*d))) / 10000000000
width = int(input("Enter the width of the tire in mm (ex 205): "))
aspect = int(input("Enter the aspect ratio of the tire (ex 60): "))
diameter = int(input("Enter the diameter of the wheel in inches (ex 15): "))

print(f"\nThe approximate volume is {volume(width,aspect,diameter):.2f} liters")

#Run again as web

print("\n> python tire_volume.py")

def volume(width,aspect,diameter):
    w = width
    a = aspect
    d = diameter
    return (math.pi * (w * w) * (a * (w*a + 2540*d))) / 10000000000
width = int(input("Enter the width of the tire in mm (ex 205): "))
aspect = int(input("Enter the aspect ratio of the tire (ex 60): "))
diameter = int(input("Enter the diameter of the wheel in inches (ex 15): "))

print(f"\nThe approximate volume is {volume(width,aspect,diameter):.2f} liters")

