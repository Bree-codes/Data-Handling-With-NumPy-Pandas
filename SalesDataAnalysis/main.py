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

# 3. Total Sales Analysis
total_units_sold = np.sum(units_sold, axis=1)  # Total units sold across all regions

top_3_indices = np.argsort(total_units_sold)[-3:]  # Indices of top 3 best-selling products
top_3_best_selling = total_units_sold[top_3_indices]

# 4. Revenue Analysis
total_revenue = np.sum(revenue)  # Overall revenue for the company

threshold = 100000  # Revenue threshold
products_above_threshold = revenue[revenue > threshold]

# 5. Profit Analysis
profit = (selling_price - cost_price) * total_units_sold  # Profit for each product

highest_profit_index = np.argmax(profit)  # Index of product with highest profit margin
lowest_profit_index = np.argmin(profit)   # Index of product with lowest profit margin

# 6. Region-wise Sales Analysis
sales_by_region = np.sum(units_sold, axis=0)  # Total units sold by region

most_sales_region = np.argmax(sales_by_region)  # Region with most sales
least_sales_region = np.argmin(sales_by_region) # Region with least sales

# 7. Simulate Sales Growth
growth_rate = np.random.uniform(0.05, 0.20, total_units_sold.shape)
new_units_sold = total_units_sold * (1 + growth_rate)
new_revenue = new_units_sold * selling_price
new_profit = new_revenue - cost_price * new_units_sold

# 8. Product Popularity
popularity_rank_units = np.argsort(total_units_sold)[::-1]  # Ranking by units sold
popularity_rank_revenue = np.argsort(revenue)[::-1]         # Ranking by revenue

# Print Results
print("Total Units Sold per Product:", total_units_sold)
print("Top 3 Best-Selling Products (Total Units Sold):", top_3_best_selling)
print("\nTotal Revenue for the Company: $", total_revenue)
print("Products Exceeding Revenue Threshold:", products_above_threshold)

"""print("\nProduct with Highest Profit Margin:", product_names[highest_profit_index])
print("Product with Lowest Profit Margin:", product_names[lowest_profit_index])"""

print("\nRegion-wise Total Sales:", sales_by_region)
print("Region with Most Sales:", most_sales_region + 1)
print("Region with Least Sales:", least_sales_region + 1)
print("\nSimulated New Units Sold:", new_units_sold)
print("Simulated New Revenue:", new_revenue)
print("\nProduct Popularity by Units Sold:", popularity_rank_units + 1)
print("Product Popularity by Revenue:", popularity_rank_revenue + 1)
