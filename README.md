# Task 2: Data Visualization and Storytelling

## Internship task
**Objective:** Create visualizations that communicate a clear story from sales data.

## Project contents
- `sales_dataset.csv` — sample raw sales dataset (contains a few missing values and duplicate rows for cleaning practice).
- `cleaned_sales_dataset.csv` — cleaned dataset.
- `task2_visualization.py` — complete Python program.
- `charts/` — four exported visualization images.
- `Sales_Visualization_Report.pdf` — visual report with key findings.

## Tools
Python, Pandas, Matplotlib, NumPy (NumPy is only needed to recreate the sample data; the analysis script uses Pandas and Matplotlib).

## Run in Pydroid 3
1. Install packages from Pip: `pandas`, `matplotlib`, `numpy`.
2. Keep `task2_visualization.py` and `sales_dataset.csv` in the same folder.
3. Open the Python file in Pydroid 3 and press Run.
4. Find the generated cleaned CSV, charts folder, and PDF in the same project folder.

You can also run on a computer:
```bash
pip install pandas matplotlib numpy
python task2_visualization.py
```

## Data cleaning performed
- Removed duplicate rows.
- Converted order dates to datetime.
- Filled missing region values with `Unknown`.
- Filled missing numeric values with each column's median.
- Removed rows missing essential order/product fields.
- Created a month field for trend analysis.

## Visualizations and why they are used
1. **Bar chart:** compares sales across product categories.
2. **Pie chart:** shows each region's share of total sales.
3. **Line chart:** shows how sales change month by month.
4. **Horizontal bar chart:** ranks the five highest-sales products.

## Key findings from this sample dataset
- Total sales: ₹343,334.20
- Total profit: ₹91,321.01
- Unique orders: 240
- Average sales per order: ₹1,430.56
- Highest-sales category: Technology
- Highest-sales region: South
- Highest-sales product among the top five: Phone

> These findings are based on the included synthetic practice dataset, not on actual company sales.

## Interview questions — short answers
1. **Why is data visualization important?** It makes patterns, comparisons, and trends easier to understand.
2. **Pie chart vs bar chart?** A pie chart shows parts of a whole; a bar chart compares values across categories.
3. **How can visuals be engaging?** Use clear titles, readable labels, suitable charts, limited colors, and highlighted insights.
4. **What is data storytelling?** Combining data, visuals, and explanation to communicate a useful message.
5. **How do you avoid misleading visuals?** Use correct scales, show context, label units, and do not hide relevant data.
6. **Dashboard best practices?** Keep it simple, organize related charts, use consistent colors, and highlight important KPIs.
7. **Which tools are used?** This project uses Python, Pandas, and Matplotlib. Tableau and Power BI are other common tools.

## Conclusion
The project demonstrates a complete beginner-friendly workflow: load sales data, clean it, analyze performance, create charts, and communicate business insights.
