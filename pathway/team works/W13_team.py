import math

def compute_area_square(side):
    return float(side)**2
    
def compute_area_rectangle(length, width):
    return float(length) * float(width)

def compute_area_circle(radius):
    return float(math.pi) * float(radius)**2
shape = None
while shape != "quit":
    shape = input("what is your shape? ")
    if shape.lower() == "square":
        side = input("What's the length of side of the square?")
        square = compute_area_square(side)
        print(f"The area of the square is: {square}")
    elif shape.lower() == "rectangle":
        length = input("What's the length of rectangle?")
        width = input("What's the width of rectangle?")
        rectangle = compute_area_rectangle(length, width)
        print(f'The area of the rectangle is: {rectangle}')
    elif shape.lower() == "circle":
        radius = input("What's the radius of the circle?")
        circle = compute_area_circle(radius)
        print(f'The area of the circle is: {circle:.2f}')
    else:
        print("please type the square, rectangle or circle only.\n")    
print("\nThank you and good bye")




