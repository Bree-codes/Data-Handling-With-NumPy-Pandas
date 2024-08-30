import numpy as np
import matplotlib.pyplot as plt

# Temperature data for City A and City B over a week
city_a_temps = np.array([22, 23, 19, 21, 25, 20, 18])
city_b_temps = np.array([30, 29, 27, 28, 26, 31, 32])

print("City A Temperatures:", city_a_temps)
print("City B Temperatures:", city_b_temps)

# Difference Between Temperatures of the Two Cities
temp_difference = city_b_temps - city_a_temps
print("Temperature Difference (City B - City A):", temp_difference)

# Convert Temperatures from Celsius to Fahrenheit
city_a_fahrenheit = city_a_temps * 9/5 + 32
city_b_fahrenheit = city_b_temps * 9/5 + 32

print("City A Temperatures in Fahrenheit:", city_a_fahrenheit)
print("City B Temperatures in Fahrenheit:", city_b_fahrenheit)

# Calculate Average Temperature for Each City
avg_temp_city_a = city_a_temps.mean()
avg_temp_city_b = city_b_temps.mean()

print("Average Temperature for City A:", avg_temp_city_a)
print("Average Temperature for City B:", avg_temp_city_b)

# Find the Day with the Maximum Temperature in City A
max_temp_city_a = city_a_temps.max()
max_temp_day_city_a = city_a_temps.argmax()

print("Max Temperature in City A:", max_temp_city_a)
print("Day of Max Temperature in City A (0=Mon, 6=Sun):", max_temp_day_city_a)

# Boolean Indexing to Find Days with Temperatures Above 25°C in City B
hot_days_city_b = city_b_temps[city_b_temps > 25]
print("Days in City B with Temperature Above 25°C:", hot_days_city_b)

# Total Temperature Over the Week for Each City
total_temp_city_a = city_a_temps.sum()
total_temp_city_b = city_b_temps.sum()

print("Total Temperature Over the Week in City A:", total_temp_city_a)
print("Total Temperature Over the Week in City B:", total_temp_city_b)

# Standard Deviation of Temperatures in City A
std_dev_city_a = city_a_temps.std()
print("Standard Deviation of Temperatures in City A:", std_dev_city_a)

# Visualization with Matplotlib
days = np.array(["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"])

plt.plot(days, city_a_temps, label="City A", marker="o")
plt.plot(days, city_b_temps, label="City B", marker="o")
plt.xlabel("Day")
plt.ylabel("Temperature (°C)")
plt.title("Temperature Comparison Between City A and City B")
plt.legend()
plt.grid(True)
plt.show()
