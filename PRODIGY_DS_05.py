import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("cleaned.csv")

sns.set(style="whitegrid")

plt.figure(figsize=(10, 6))
sns.countplot(y='Weather_conditions', data=df, order=df['Weather_conditions'].value_counts().index, palette="coolwarm")
plt.title("Accidents by Weather Conditions")
plt.xlabel("Number of Accidents")
plt.ylabel("Weather Condition")
plt.tight_layout()
plt.savefig("weather_conditions.png")
plt.show()

plt.figure(figsize=(10, 6))
sns.countplot(y='Road_surface_type', data=df, order=df['Road_surface_type'].value_counts().index, palette="Blues_r")
plt.title("Accidents by Road Surface Type")
plt.xlabel("Number of Accidents")
plt.ylabel("Road Surface Type")
plt.tight_layout()
plt.savefig("road_surface_type.png")
plt.show()

plt.figure(figsize=(10, 6))
sns.countplot(y='Light_conditions', data=df, order=df['Light_conditions'].value_counts().index, palette="YlGnBu")
plt.title("Accidents by Light Conditions")
plt.xlabel("Number of Accidents")
plt.ylabel("Light Condition")
plt.tight_layout()
plt.savefig("light_conditions.png")
plt.show()

plt.figure(figsize=(10, 6))
sns.countplot(y='Type_of_collision', data=df, order=df['Type_of_collision'].value_counts().index, palette="OrRd")
plt.title("Types of Collision")
plt.xlabel("Number of Accidents")
plt.ylabel("Type of Collision")
plt.tight_layout()
plt.savefig("type_of_collision.png")
plt.show()

plt.figure(figsize=(10, 6))
sns.countplot(y='Cause_of_accident', data=df, order=df['Cause_of_accident'].value_counts().index[:10], palette="PuBu")
plt.title("Top 10 Causes of Accidents")
plt.xlabel("Number of Accidents")
plt.ylabel("Cause of Accident")
plt.tight_layout()
plt.savefig("cause_of_accident.png")
plt.show()

plt.figure(figsize=(12, 6))
sns.countplot(data=df, x='Accident_severity', hue='Light_conditions', palette="Set2")
plt.title("Accident Severity by Light Conditions")
plt.xlabel("Severity")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("severity_by_light.png")
plt.show()

print("Visualizations generated and displayed.")
