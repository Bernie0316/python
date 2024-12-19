def water_column_height(tower_height, tank_height):
    t = tower_height # t is the height of the tower
    w = tank_height # w is the height of the walls of the tank that is on top of the tower
    h = t + (w*3) / 4 # h is height of the water column 
    return h

def pressure_gain_from_water_height(height):
    h = height # h is the height of the water column in meters
    g = 9.80665 # g is the acceleration from Earths gravity (9.80665 meter / second2)
    p = 998.2 # ρ is the density of water (998.2 kilogram / meter3)
    P = ((p*g*h) /1000) # P is the pressure in kilopascals
    return P 

def reynolds_number(hydraulic_diameter, fluid_velocity):
    p = 998.2 # ρ is the density of water (998.2 kilogram / meter3)
    d = hydraulic_diameter # d is the hydraulic diameter of a pipe in meters. For a round pipe, the hydraulic diameter is the same as the pipe’s inner diameter.
    v = fluid_velocity # v is the velocity of the water flowing through the pipe in meters / second
    wdv = 0.0010016 # μ is the dynamic viscosity of water (0.0010016 Pascal seconds)
    R = p * d * v / wdv # R is the Reynolds number
    return R

def pressure_loss_from_pipe(pipe_diameter,
        pipe_length, friction_factor, fluid_velocity):
    d = pipe_diameter # d is the diameter of the pipe in meters 
    v = fluid_velocity # v is the velocity of the water flowing through the pipe in meters / second
    p = 998.2 # ρ is the density of water (998.2 kilogram / meter3)
    l = pipe_length # L is the length of the pipe in meters
    f = friction_factor # f is the pipe’s friction factor
    P = ((-f*l*p*(v*v) / (2000*d))) # P is the lost pressure in kilopascals
    return P

def pressure_loss_from_fittings(
        fluid_velocity, quantity_fittings):
    n = quantity_fittings # n is the quantity of fittings
    v = fluid_velocity # v is the velocity of the water flowing through the pipe in meters / second
    p = 998.2 # ρ is the density of water (998.2 kilogram / meter3)
    P = (-0.04*p*(v*v)*n) /2000 # P is the lost pressure in kilopascals
    return P


def pressure_loss_from_pipe_reduction(larger_diameter,
        fluid_velocity, reynolds_number, smaller_diameter):
    # k is a constant computed by the first formula and used in the second formula
    # R is the Reynolds number that corresponds to the pipe with the larger diameter
    # D is the diameter of the larger pipe in meters
    # d is the diameter of the smaller pipe in meters
    # P is the lost pressure kilopascals
    # wd is the density of water (998.2 kilogram / meter3)
    # v is the velocity of the water flowing through the larger diameter pipe in meters / second
    R = reynolds_number
    p = 998.2
    d = smaller_diameter
    D = larger_diameter
    v = fluid_velocity
    k = (0.1 + (50/R)) * ((D/d)**4 - 1)
    P = -k * p * (v**2) / 2000
    return P

PVC_SCHED80_INNER_DIAMETER = 0.28687 # (meters)  11.294 inches
PVC_SCHED80_FRICTION_FACTOR = 0.013  # (unitless)
SUPPLY_VELOCITY = 1.65               # (meters / second)

HDPE_SDR11_INNER_DIAMETER = 0.048692 # (meters)  1.917 inches
HDPE_SDR11_FRICTION_FACTOR = 0.018   # (unitless)
HOUSEHOLD_VELOCITY = 1.75            # (meters / second)

def main():
    tower_height = float(input("Height of water tower (meters): "))
    tank_height = float(input("Height of water tank walls (meters): "))
    length1 = float(input("Length of supply pipe from tank to lot (meters): "))
    quantity_angles = int(input("Number of 90° angles in supply pipe: "))
    length2 = float(input("Length of pipe from supply to house (meters): "))

    water_height = water_column_height(tower_height, tank_height)
    pressure = pressure_gain_from_water_height(water_height)

    diameter = PVC_SCHED80_INNER_DIAMETER
    friction = PVC_SCHED80_FRICTION_FACTOR
    velocity = SUPPLY_VELOCITY
    reynolds = reynolds_number(diameter, velocity)
    loss = pressure_loss_from_pipe(diameter, length1, friction, velocity)
    pressure += loss

    loss = pressure_loss_from_fittings(velocity, quantity_angles)
    pressure += loss

    loss = pressure_loss_from_pipe_reduction(diameter,
            velocity, reynolds, HDPE_SDR11_INNER_DIAMETER)
    pressure += loss

    diameter = HDPE_SDR11_INNER_DIAMETER
    friction = HDPE_SDR11_FRICTION_FACTOR
    velocity = HOUSEHOLD_VELOCITY
    loss = pressure_loss_from_pipe(diameter, length2, friction, velocity)
    pressure += loss

    print(f"Pressure at house: {pressure:.1f} kilopascals")


if __name__ == "__main__":
    main()
