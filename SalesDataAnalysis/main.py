#Analyzing sales for a company

import numpy as np

# Product ID
product_id = np.array([101, 102, 103, 104, 105, 106, 107, 108, 109, 110])

# Product Name (stored as a list since NumPy is not ideal for strings)
product_name = [
    "SmartPhone X1", "Laptop Pro V5", "Wireless Earbuds Z2", "4K Ultra HD TV",
    "Gaming Console X", "Smart Home Hub 2.0", "Fitness Tracker Z5",
    "Tablet Lite 10", "VR Headset Pro", "Smartwatch Series 4"
]

# Units Sold in 4 Regions
units_sold = np.array([
    [120, 150, 140, 110],
    [90, 85, 100, 95],
    [200, 180, 210, 190],
    [60, 55, 65, 50],
    [130, 120, 140, 135],
    [110, 115, 100, 105],
    [160, 150, 155, 145],
    [75, 70, 80, 85],
    [50, 55, 60, 45],
    [140, 135, 130, 120]
])

# Revenue
revenue = np.array([80000, 120000, 70000, 200000, 150000, 55000, 60000, 100000, 150000, 90000])

# Cost Price
cost_price = np.array([500, 700, 100, 1000, 500, 200, 150, 500, 800, 300])

# Selling Price
selling_price = np.array([800, 1200, 350, 2500, 1000, 550, 400, 1000, 2000, 600])

# Total units sold for each product (sum across regions)
total_units_sold = np.sum(units_sold, axis=1)
print(f"The total units sold are: {total_units_sold}")



