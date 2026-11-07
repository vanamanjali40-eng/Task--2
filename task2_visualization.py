"""
Task 2: Data Visualization and Storytelling
Run: python task2_visualization.py
Input: sales_dataset.csv (same folder)
Outputs: cleaned_sales_dataset.csv, charts/*.png, Sales_Visualization_Report.pdf
"""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

BASE = Path(__file__).resolve().parent
CHART_DIR = BASE / "charts"
CHART_DIR.mkdir(exist_ok=True)

# 1. Load data
df = pd.read_csv(BASE / "sales_dataset.csv")
print("Original shape:", df.shape)

# 2. Clean data
df["Order_Date"] = pd.to_datetime(df["Order_Date"], errors="coerce")
df = df.drop_duplicates()
df["Region"] = df["Region"].fillna("Unknown")
for col in ["Sales", "Profit", "Quantity", "Discount"]:
    df[col] = pd.to_numeric(df[col], errors="coerce")
    df[col] = df[col].fillna(df[col].median())
df = df.dropna(subset=["Order_ID", "Order_Date", "Category", "Product"])
df["Month"] = df["Order_Date"].dt.to_period("M").astype(str)
df.to_csv(BASE / "cleaned_sales_dataset.csv", index=False)
print("Cleaned shape:", df.shape)

# 3. Analyze
total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
total_orders = df["Order_ID"].nunique()
avg_order_value = total_sales / total_orders if total_orders else 0
category_sales = df.groupby("Category")["Sales"].sum().sort_values(ascending=False)
region_sales = df.groupby("Region")["Sales"].sum().sort_values(ascending=False)
monthly_sales = df.groupby("Month")["Sales"].sum().sort_index()
product_sales = df.groupby("Product")["Sales"].sum().sort_values(ascending=False).head(5)

print("\\nKEY PERFORMANCE INDICATORS")
print(f"Total sales: ₹{total_sales:,.2f}")
print(f"Total profit: ₹{total_profit:,.2f}")
print(f"Unique orders: {total_orders}")
print(f"Average sales per order: ₹{avg_order_value:,.2f}")
print("\\nSales by category:\\n", category_sales)
print("\\nSales by region:\\n", region_sales)
print("\\nTop products:\\n", product_sales)

# 4. Visualizations
with PdfPages(BASE / "Sales_Visualization_Report.pdf") as pdf:
    # Category bar chart
    fig, ax = plt.subplots(figsize=(9, 5))
    category_sales.plot(kind="bar", ax=ax, color="#4C78A8")
    ax.set_title("Sales by Product Category")
    ax.set_xlabel("Category"); ax.set_ylabel("Sales (₹)")
    ax.tick_params(axis="x", rotation=15)
    ax.grid(axis="y", alpha=.25)
    fig.tight_layout()
    fig.savefig(CHART_DIR / "01_category_sales.png", dpi=160)
    pdf.savefig(fig); plt.close(fig)

    # Regional pie chart
    fig, ax = plt.subplots(figsize=(7, 5))
    region_sales.plot(kind="pie", autopct="%1.1f%%", startangle=90, ax=ax,
                      colors=["#4C78A8", "#F58518", "#54A24B", "#E45756", "#B279A2"])
    ax.set_title("Share of Sales by Region"); ax.set_ylabel("")
    fig.tight_layout()
    fig.savefig(CHART_DIR / "02_region_sales.png", dpi=160)
    pdf.savefig(fig); plt.close(fig)

    # Monthly trend
    fig, ax = plt.subplots(figsize=(10, 5))
    monthly_sales.plot(kind="line", marker="o", linewidth=2, ax=ax, color="#54A24B")
    ax.set_title("Monthly Sales Trend")
    ax.set_xlabel("Month"); ax.set_ylabel("Sales (₹)")
    ax.tick_params(axis="x", rotation=45); ax.grid(alpha=.25)
    fig.tight_layout()
    fig.savefig(CHART_DIR / "03_monthly_sales.png", dpi=160)
    pdf.savefig(fig); plt.close(fig)

    # Top products horizontal bars
    fig, ax = plt.subplots(figsize=(9, 5))
    product_sales.sort_values().plot(kind="barh", ax=ax, color="#F58518")
    ax.set_title("Top 5 Products by Sales")
    ax.set_xlabel("Sales (₹)"); ax.set_ylabel("Product")
    ax.grid(axis="x", alpha=.25)
    fig.tight_layout()
    fig.savefig(CHART_DIR / "04_top_products.png", dpi=160)
    pdf.savefig(fig); plt.close(fig)

# 5. Business insights
print("\\nBUSINESS INSIGHTS")
print("Highest-sales category:", category_sales.idxmax())
print("Highest-sales region:", region_sales.idxmax())
print("Top product:", product_sales.idxmax())
print("The monthly trend can help identify stronger and weaker sales periods.")
print("\\nProject completed. Check the generated CSV, charts folder, and PDF report.")
