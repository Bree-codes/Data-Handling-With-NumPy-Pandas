import pandas as pd

data = {
    'Transaction_ID': ['T001', 'T002', 'T003', 'T004', 'T005', 'T006', 'T007', 'T008', 'T009', 'T010'],
    'Customer_Name': ['Alice', 'Bob', 'Charlie', 'Dave', 'Eve', 'Frank', 'Grace', 'Heidi', 'Ivan', 'Judy'],
    'Product': ['Laptop', 'Smartphone', 'Headphones', 'Tablet', 'Laptop', 'Smartphone', 'Headphones', 'Tablet', 'Laptop', 'Smartphone'],
    'Quantity': [1, 2, 5, 1, 2, 1, 3, 4, 1, 2],
    'Price': [1200, 800, 100, 500, 1200, 800, 100, 500, 1200, 800],
    'Date': ['2024-09-01', '2024-09-02', '2024-09-03', '2024-09-04', '2024-09-05', '2024-09-06', '2024-09-07', '2024-09-08', '2024-09-09', '2024-09-10'],
    'Location': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
}

df = pd.DataFrame(data)
print(df)

print("\nQuantity Column:\n", df['Quantity'])