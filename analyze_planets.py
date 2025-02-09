import numpy as np  # Import NumPy
import pandas as pd  # Import Pandas to read CSV files

# Load the planetary data into a Pandas DataFrame
df = pd.read_csv("planetary_data.csv")

# Convert columns to NumPy arrays
temperatures = np.array(df["Temperature_C"])
gravities = np.array(df["Gravity_mps2"])
atmospheres = np.array(df["Atmosphere_Density"])

# Calculate statistics
average_temp = np.mean(temperatures)
max_gravity = np.max(gravities)
min_atmosphere = np.min(atmospheres)

# Display results
print("🌍 Average Planet Temperature:", average_temp, "°C")
print("🪐 Max Gravity Found:", max_gravity, "m/s²")
print("☁️ Thinnest Atmosphere Density:", min_atmosphere)
