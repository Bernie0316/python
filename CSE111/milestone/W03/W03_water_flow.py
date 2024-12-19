# 01 In your water_flow.py program, write a function named water_column_height that calculates and returns the height of a column of water from a tower height and a tank wall height. The function must have this header:
# In your function, use the following formula for calculating the water column height.
def water_column_height(tower_height, tank_height):
    t = tower_height # t is the height of the tower
    w = tank_height # w is the height of the walls of the tank that is on top of the tower
    h = t + (w*3) / 4 # h is height of the water column 
    return h

def pressure_gain_from_water_height(height):
    # P is the pressure in kilopascals
    # ρ is the density of water (998.2 kilogram / meter3)
    # g is the acceleration from Earths gravity (9.80665 meter / second2)
    # h is the height of the water column in meters
    h = height
    g = 9.80665
    p = 998.2
    P = ((p*g*h) /1000)
    return P 

def pressure_loss_from_pipe(pipe_diameter,
        pipe_length, friction_factor, fluid_velocity):
    # P is the lost pressure in kilopascals
    # f is the pipe’s friction factor
    # L is the length of the pipe in meters
    # ρ is the density of water (998.2 kilogram / meter3)
    # v is the velocity of the water flowing through the pipe in meters / second
    # d is the diameter of the pipe in meters 
    d = pipe_diameter
    v = fluid_velocity
    p = 998.2
    l = pipe_length
    f = friction_factor
    P = ((-f*l*p*(v*v) / (2000*d)))
    return P

