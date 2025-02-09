import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import optimize  # Import SciPy optimization module
from bloom_filter import BloomFilter

# Creating a planetary database
data = {
    "Planet": ["Mars", "Venus", "Jupiter", "Saturn", "Mercury", "Neptune"],
    "Gravity (m/s²)": [3.71, 8.87, 24.79, 10.44, 3.7, 11.15],
    "Has Atmosphere": [True, True, True, True, False, True]
}

df = pd.DataFrame(data)

# Create a bloom filter to track visited planets
bloom = BloomFilter(max_elements=10, error_rate=0.1)

# Mark some planets as visited
visited_planets = ["Mars", "Venus"]
for planet in visited_planets:
    bloom.add(planet)

# Filter out planets that are in the bloom filter (already visited)
unvisited_planets = df[~df["Planet"].apply(lambda p: p in bloom)]

# Save unvisited planets to a CSV file
unvisited_planets.to_csv("unvisited_planets.csv", index=False)

# ---------- SciPy Optimization ----------
# Find the planet with the best gravity using SciPy's optimization

# The function to minimize (we want to maximize gravity, so we minimize the negative gravity)
def gravity_function(planet_name):
    planet_data = df[df['Planet'] == planet_name]
    return -planet_data['Gravity (m/s²)'].values[1]  # Negative because we want to maximize gravity

# Use SciPy to find the planet with the best gravity
best_planet = optimize.fminbound(gravity_function, 0, len(df)-1)

# Get the name of the best planet (using the index)
best_planet_name = df.iloc[int(best_planet)]['Planet']
best_gravity = df.iloc[int(best_planet)]['Gravity (m/s²)']

print(f"🚀 The best planet for building a space station is {best_planet_name} with gravity {best_gravity} m/s²!")

# ---------- Matplotlib Visualization ----------
plt.figure(figsize=(8, 5))
plt.bar(unvisited_planets["Planet"], np.array(unvisited_planets["Gravity (m/s²)"]), color='skyblue')
plt.title('Gravity of Unvisited Planets')
plt.xlabel('Planet')
plt.ylabel('Gravity (m/s²)')
plt.show()

# ---------- Seaborn Visualization ----------
plt.figure(figsize=(8, 5))
sns.scatterplot(x="Gravity (m/s²)", y="Has Atmosphere", data=unvisited_planets, hue="Has Atmosphere", palette="viridis")
plt.title('Gravity vs Atmosphere Presence for Unvisited Planets')
plt.xlabel('Gravity (m/s²)')
plt.ylabel('Has Atmosphere')
plt.show()
