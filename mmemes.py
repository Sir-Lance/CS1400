import math
radius = int(input())

def sphereArea(radius):
    area = 4 * math.pi * radius ** 2
    print(area, "ft2")
sphereArea(radius)

def sphereVolume(radius):
    volume = 4 / 3 * math.pi * radius ** 3
    print(volume, "ft3")
sphereVolume(radius)
