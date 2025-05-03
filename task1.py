###
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = celsius_to_fahrenheit(celsius)

print(f"{celsius}°C is equal to {fahrenheit}°F")

####
###2
import math

def calculate_distance(x1, y1, x2, y2):
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance

print("Enter the coordinates of the first point (x1, y1):")
x1 = float(input("x1: "))
y1 = float(input("y1: "))

print("Enter the coordinates of the second point (x2, y2):")
x2 = float(input("x2: "))
y2 = float(input("y2: "))

distance = calculate_distance(x1, y1, x2, y2)
print(f"The Euclidean distance between the points is: {distance:.2f}")
###3
def calculate_glasses_of_milk():
    height = float(input("Enter the height of the milk tank "))
    width = float(input("Enter the width of the milk tank"))
    breadth = float(input("Enter the breadth of the milk tank"))

    glass_capacity = float(input("Enter the capacity of one glass"))

    tank_volume = height * width * breadth
    num_glasses = tank_volume // glass_capacity

    print(f"Number of glasses of milk that can be obtained: {int(num_glasses)}")
calculate_glasses_of_milk() 

###4
def sum_of_fractions(a,b,c,d):
  sum_of_fractions = (a*b)+(c*d)/(b*d)
  return sum_of_fractions
a=int(input("Enter the numerator of the first fraction: "))
b=int(input("Enter the denominator of the second fraction: "))
c=int(input("Enter the numerator of the third fraction: "))
d=int(input("Enter the denominator of the forth fraction: "))
sum = sum_of_fractions(a,b,c,d)
print("The sum of the fractions is:",sum)