length = int(input())
width = int(input())
height = int(input())
percentage = float(input())

volume_of_aquarium = (length * width * height) / 1000
liters_of_water = volume_of_aquarium * ((100 - percentage) / 100)
print(liters_of_water)