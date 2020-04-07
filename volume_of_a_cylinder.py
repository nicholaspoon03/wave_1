import math
radius = float(input('Radius: '))
height = float(input('Height: '))
volume = math.pi * (radius ** 2) * height
print(round(volume, 1), 'square units')