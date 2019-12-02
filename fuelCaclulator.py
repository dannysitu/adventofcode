import array as arr
import math

def calculateFuel(masses):
    fuelSum = 0;
    
    for x in masses:
        mass = math.floor(int(x)/3);
        mass = mass - 2;
        
        if (mass > 0):
            fuelSum = fuelSum + calculateFuel(arr.array('i', [mass])) + mass;
    
    return fuelSum;

masses = input("Input mass(comma deliminated): ");

masses = masses.split(",");

print(calculateFuel(masses));
