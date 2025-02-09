import numpy as np
from numpy.ma.extras import average

# Create a simple array of spaceship fuel levels
fuel_levels = np.array([80, 90, 70, 65, 100])

#Perform calculations
average_fuel = np.mean(fuel_levels)
max_fuel = np.max(fuel_levels)

print("Average fuel level:", average_fuel)
print("Max fuel level:", max_fuel)