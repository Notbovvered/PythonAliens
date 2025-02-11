import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import optimize  # Import SciPy optimization module
from bloom_filter import BloomFilter
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Creating a planetary database
data = {
    "Planet": ["Mars", "Venus", "Jupiter", "Saturn", "Mercury", "Neptune"],
    "Gravity (m/s²)": [3.71, 8.87, 24.79, 10.44, 3.7, 11.15],
    "Has Atmosphere": [1, 1, 1, 1, 0, 1] # 1 has atmosphere, 0 = none
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
    return -planet_data['Gravity (m/s²)'].values[0]  # Negative because we want to maximize gravity

# Use SciPy to find the planet with the best gravity
best_planet = optimize.fminbound(gravity_function, 0, len(df)-1)

# Get the name of the best planet (using the index)
best_planet_name = df.iloc[int(best_planet)]['Planet']
best_gravity = df.iloc[int(best_planet)]['Gravity (m/s²)']

print(f"🚀 The best planet for building a space station is {best_planet_name} with gravity {best_gravity} m/s²!")

# ---------- Machine Learning with Scikit-learn ----------
# Prepare data for classification
X = df[['Gravity (m/s²)']]  # Feature (gravity)
y = df['Has Atmosphere']    # Target (1 = Yes, 0 = No)

# Split into training (80%) and testing (20%) data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# train a logistic regression model
model = LogisticRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evalute the model
accuracy = accuracy_score(y_test, y_pred)
print(f"AI Accuracy in Predicting Atmospheres: {accuracy * 100:.2f}%")

# Predict atmosphere presence for unvisited planets
unvisited_X = unvisited_planets[['Gravity (m/s²)']]
predicted_atmosphere = model.predict(unvisited_X)
unvisited_planets["Predicted Atmosphere"] = predicted_atmosphere

print("Predictions for Unvisited Planets:")
print(unvisited_planets)

# Save new predictions to file
unvisited_planets.to_csv("unvisited_planets_with_predictions.csv", index=False)
print("Data saved to unvisited_planets_with_predictions.csv")

# ---------- Matplotlib & Seaborn Visualization ----------
plt.figure(figsize=(8, 5))
sns.scatterplot(x="Gravity (m/s²)", y="Predicted Atmosphere", data=unvisited_planets, hue="Predicted Atmosphere", palette="coolwarm")
plt.title('Predicted Atmosphere vs Gravity')
plt.xlabel('Gravity (m/s²)')
plt.ylabel('Predicted Atmosphere (1 = Yes, 0 = No)')
plt.show()
