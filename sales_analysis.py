import pandas as pd
import matplotlib.pyplot as plt
import random

# ----------------------------------------
# 1. Function to generate synthetic data
# ----------------------------------------
def generate_sales_data(num_records=1500):
    customer_names = [
        "John Smith", "Sara Lee", "Alex Brown", "Maria Garcia", "James Wilson",
        "Linda Kim", "Robert Davis", "Emily White", "David Thompson", "Ana Martinez",
        "Tom Clark", "Sophie Turner", "Daniel Evans", "Laura Scott", "Chris Taylor"
    ]
    countries = ["USA", "Canada", "Mexico", "UK", "Spain", "Australia"]
    products = [
        ("Laptop", 1200), ("Smartphone", 800), ("Tablet", 500),
        ("Headphones", 150), ("Smartwatch", 250)
    ]

    data = []
    for i in range(num_records):
        name = random.choice(customer_names)
        country = random.choice(countries)
        product, price = random.choice(products)
        quantity = random.randint(1, 3)
        data.append({
            "CustomerID": 100 + i,
            "Name": name,
            "Country": country,
            "Product": product,
            "Quantity": quantity,
            "Price": price
        })
    
    return pd.DataFrame(data)

# -------------------------------
# 2. Generate data & save CSV
# -------------------------------
df = generate_sales_data(1500)
df.to_csv("sales_data.csv", index=False)
print("Dataset created: sales_data.csv")
print(df.head())

# -------------------------------
# 3. Analysis
# -------------------------------
df["Total"] = df["Quantity"] * df["Price"]

total_revenue = df["Total"].sum()
customers_by_country = df["Country"].value_counts()
top_product = df["Product"].value_counts().idxmax()

print(f"Total revenue: ${total_revenue}")
print("Customers by country:")
print(customers_by_country)
print(f"Most popular product: {top_product}")

# -------------------------------
# 4. Visualization
# -------------------------------
# Bar chart: revenue by product
revenue_by_product = df.groupby("Product")["Total"].sum()
revenue_by_product.plot(kind="bar")
plt.title("Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Revenue ($)")
plt.tight_layout()
plt.savefig("revenue_by_product.png")
plt.close()

# Pie chart: customers by country
customers_by_country.plot(kind="pie", autopct="%1.1f%%")
plt.title("Customers by Country")
plt.ylabel("")
plt.tight_layout()
plt.savefig("customers_by_country.png")
plt.close()

print("Charts saved: revenue_by_product.png, customers_by_country.png")