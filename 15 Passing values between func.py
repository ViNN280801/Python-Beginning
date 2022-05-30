# Importing module "math"
import math

# Returns radius from input
def get_radius():
    radius = float(input('Enter diamter of base of cylinder: '))
    radius /= 2
    return radius

# Returns forming of cylinder from input
def get_forming():
    forming = float(input('Enter forming of cylinder: '))
    return forming

# Returns volume of cylinder
def calc_cylinder_volume():
    r = get_radius()
    h = get_forming()
    S = math.pi * math.pow(r, 2)
    return S * h

# Prints cylinder volume
def cylinder_volume():
    print('Volume of cylinder equals ' + str(calc_cylinder_volume()) + ' volume units')

# Return weight of solid cylinder
def get_cylinder_weight(volume):
    density = float(input('Enter density of cylinder\' material: '))
    return volume * density

print('Weight of solid cylinder is ' + str(get_cylinder_weight(calc_cylinder_volume())))

# Conclusion: It's necessary to write the code in such a way as to avoid working with global scope
