import pandas as pd
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

# Save unvisted planets to a csv file
unvisited_planets.to_csv("unvisited_planets.csv", index=False)

print("Planets you haven't visited yet: ")
print(unvisited_planets)
print("Data saved to unvisited_planets.csv")