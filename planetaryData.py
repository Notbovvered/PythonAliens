import pandas as pd
import numpy as np
from bloom_filter import BloomFilter

# Creating a planetary database
data = {
    "Planet": ["Mars", "Venus", "Jupiter", "Saturn", "Mercury", "Neptune"],
    "Gravity (m/s²)": [3.71, 8.87, 24.79, 10.44, 3.7, 11.15],
    "Has Atmosphere": [True, True, True, True, False, True]
}

df = pd.DataFrame(data)  # Convert data to a DataFrame

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

# ---------- NumPy Analysis ----------
# Convert gravity column to a NumPy array
gravity_values = np.array(unvisited_planets["Gravity (m/s²)"])

# Calculate statistics
average_gravity = np.mean(gravity_values)  # Average gravity of unvisited planets
max_gravity = np.max(gravity_values)  # Planet with highest gravity
min_gravity = np.min(gravity_values)  # Planet with lowest gravity

# Display results
print("🌍 Planets you haven't visited yet:")
print(unvisited_planets)
print("\n📊 NumPy Analysis of Unvisited Planets:")
print(f"🔢 Average Gravity: {average_gravity:.2f} m/s²")
print(f"⬆️ Highest Gravity: {max_gravity:.2f} m/s²")
print(f"⬇️ Lowest Gravity: {min_gravity:.2f} m/s²")

print("📁 Data saved to unvisited_planets.csv")
