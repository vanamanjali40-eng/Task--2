"""
DATA VISUALIZATION AND STORYTELLING
Run this file in Pydroid 3.
Keep superstore.csv in the same folder as this Python file.
"""

import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# 1. Load the dataset
file_path = Path(__file__).resolve().parent / "superstore.csv"
df = pd.read_csv(file_path)

# 2. Prepare the data
df["Order_Date"] = pd.to_datetime(df["Order_Date"], errors="coerce")
df["Sales"] = pd.to_numeric(df["Sales"], errors="coerce")
df["Profit"] = pd.to_numeric(df["Profit"], errors="coerce")
df["Quantity"] = pd.to_numeric(df["Quantity"], errors="coerce")
df = df.dropna(subset=["Order_Date", "Sales", "Profit", "Quantity"])

# 3. Calculate key business figures
total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
total_orders = len(df)
total_quantity = df["Quantity"].sum()
average_order_value = total_sales / total_orders if total_orders else 0

print("\\n========== SALES DASHBOARD SUMMARY ==========")
print("Total sales       : Rs.", round(total_sales, 2))
print("Total profit      : Rs.", round(total_profit, 2))
print("Number of orders  :", total_orders)
print("Units sold        :", int(total_quantity))
print("Average order sale: Rs.", round(average_order_value, 2))

# 4. Sales by month
df["Month"] = df["Order_Date"].dt.to_period("M").astype(str)
monthly_sales = df.groupby("Month")["Sales"].sum()

plt.figure(figsize=(10, 5))
monthly_sales.plot(kind="line", marker="o")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales (Rs.)")
plt.xticks(rotation=45)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("monthly_sales.png")
plt.show()

# 5. Sales by product category
category_sales = df.groupby("Category")["Sales"].sum().sort_values(ascending=False)

plt.figure(figsize=(8, 5))
category_sales.plot(kind="bar")
plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales (Rs.)")
plt.xticks(rotation=20)
plt.tight_layout()
plt.savefig("category_sales.png")
plt.show()

# 6. Profit by region
region_profit = df.groupby("Region")["Profit"].sum().sort_values(ascending=False)

plt.figure(figsize=(8, 5))
region_profit.plot(kind="bar")
plt.title("Profit by Region")
plt.xlabel("Region")
plt.ylabel("Profit (Rs.)")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("profit_by_region.png")
plt.show()

# 7. Sales share by category
plt.figure(figsize=(7, 7))
category_sales.plot(kind="pie", autopct="%1.1f%%", startangle=90)
plt.title("Category-wise Share of Sales")
plt.ylabel("")
plt.tight_layout()
plt.savefig("category_share.png")
plt.show()

# 8. Print insights for the story
best_category = category_sales.idxmax()
best_region = region_profit.idxmax()
best_month = monthly_sales.idxmax()
lowest_profit_region = region_profit.idxmin()

print("\\n============== BUSINESS INSIGHTS ==============")
print("1. Highest sales category :", best_category)
print("2. Highest profit region  :", best_region)
print("3. Best sales month       :", best_month)
print("4. Lowest profit region   :", lowest_profit_region)
print("\\nSTORY:")
print("The charts show how sales change over time, which category")
print("contributes most to revenue, and which region earns the most profit.")
print("The business can use these findings to plan stock, promotions,")
print("and regional sales strategies.")
print("\\nCharts saved as PNG files in the project folder.")
