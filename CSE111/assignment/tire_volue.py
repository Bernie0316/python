# 1. Gets the current date from the computer’s operating system.
from datetime import datetime
current_date_and_time = datetime.now()
print("> python tire_volume.py")

print("Wellcome to tire shore, just let me now the size of your tire\n")
import math
def volume(width,aspect,diameter):
    w = width
    a = aspect
    d = diameter
    return (math.pi * (w * w) * (a * (w*a + 2540*d))) / 10000000000
# data inputs
width = int(input("Enter the width of the tire in mm (ex 205): "))
aspect = int(input("Enter the aspect ratio of the tire (ex 60): "))
diameter = int(input("Enter the diameter of the wheel in inches (ex 15): "))
tire_volume = volume(width,aspect,diameter)
print(f"\nThe approximate volume is {tire_volume:.2f} liters")

if tire_volume > 12 and tire_volume < 15:
    print("S100")
elif tire_volume < 16 and tire_volume < 20:
    print("$250")
elif tire_volume < 20 and tire_volume < 26:
    print("$400")    
else:
    print("Em....seems like we don't this size for your tire right now,\n but we can help get the tire if you willing to wait.")

buy = input("Do you want to buy tires?(yes/no): ")

if buy == "yes":
    number = input("What is your phone number? ")
    # 2. Opens a text file named volumes.txt for appending.
    with open('volumes.txt', 'at') as volumes_file:
        # 3. Appends to the end of the volumes.txt file one line of text that contains the following five values:
        # a.current date
        # b. width of the tire
        # c. aspect ratio of the tire
        # d. diameter of the wheel
        # e. volume of the tire
        print(f'{current_date_and_time:%Y-%m-%d}",{width},{aspect},{diameter},{tire_volume:.2f},{number}', file=volumes_file)
else:
    print("Bye")  
    with open('volumes.txt', 'at') as volumes_file:
        print(f'{current_date_and_time:%Y-%m-%d}",{width},{aspect},{diameter},{tire_volume:.2f},', file=volumes_file)
  

