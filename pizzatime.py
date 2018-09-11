import math

size = int(input("Input radius of the pizza: "))
pricesq = 0.13
area = int(math.pi*size**2)
print(area * pricesq)
