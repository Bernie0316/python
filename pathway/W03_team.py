#area of the square formula is a2
#length_square = input('What is the length of a side of the square? ')
#square = float(length_square) ** 2
#print (f'The area of the square is {square}')
#area of the rectangle formula is l x w
#length_rectangle = input('What is the length of rectangle? ')
#width_rectangle = input('What is the width of rectangle? ')
#rectangle = float(length_rectangle) * float(width_rectangle)
#print (f'The area of the rectangle is {rectangle}')
#area of the circle formula is pi*r**2
import math
radius = input('What is the radius of the circle? ')
circle = float(math.pi) * float(radius) ** 2
print (f'The area of the circle is {circle}')
print ()
#Stretch challenge number 3 - display in cm2 and m2
length_square = input('What is the length of a side of the square in cm? ')
square = float(length_square) ** 2
print (f'The area of the square is: {square} cm2')
print (f'The area of the square is: {square/10000} m2')
print ()
length = float(input('Enter a length value:'))
pi = float(math.pi)
#area of a square
#volume of a sphere is 4/3 * pi * r3
print (f'The area of the square is {length**2}')
print (f'The volume of the cube is {length**3}')
print (f'The volume of the sphere is {length**3*pi*4/3}')