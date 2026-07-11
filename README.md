# Sales & Revenue Analysis Dashboard 📊

## Project Overview
This project is an end-to-end Data Analytics portfolio project designed to analyze sales performance, revenue trends, customer behavior, and profitability for a fictitious retail company. Built using Microsoft Power BI, this interactive dashboard empowers stakeholders with actionable insights to drive data-driven decision-making. 

## Features
- **Executive Dashboard:** High-level KPIs, revenue trends, and category performance.
- **Regional Analysis:** Geographical breakdown of sales and profit with drill-through capabilities.
- **Product Analysis:** Deep dive into top/bottom performing products and categories.
- **Customer Analysis:** Insights into customer segments, repeat customers, and purchasing behavior.
- **Interactive Slicers:** Dynamic filtering by Date, Region, Category, and Customer Segment.

## Dashboard Screenshots
*(Replace the image below with a screenshot of your final Power BI dashboard)*

![Dashboard](Images/dashboard.png)

## Tools Used
- **Microsoft Power BI Desktop:** For data visualization, DAX, and dashboard creation.
- **Power Query:** For data cleaning and transformation.
- **Python / CSV:** For generating and storing the 10,000+ records dataset.
- **GitHub:** For version control and portfolio showcasing.

## Dataset Description
The dataset contains 10,000 sales records generated to simulate a real-world retail environment.
- **Order & Shipping:** Order ID, Order Date, Ship Date, Shipping Mode
- **Customer:** Customer ID, Customer Name, Segment
- **Geography:** Country, State, City, Region
- **Product:** Product ID, Category, Sub Category, Product Name
- **Financials:** Quantity, Unit Price, Discount, Sales, Cost, Profit, Profit Margin, Payment Mode

## Key Performance Indicators (KPIs)
- **Total Sales:** Overall sales value generated.
- **Total Revenue:** Net revenue after discounts.
- **Total Profit:** Overall profit achieved.
- **Total Orders:** Count of unique orders.
- **Average Order Value (AOV):** Average revenue per order.
- **Profit Margin %:** Profit as a percentage of total sales.

## Charts & Visualizations
- **Monthly Sales & Profit Trend:** Line charts to identify seasonal trends.
- **Revenue by Region & State:** Bar and Map visuals for geographical analysis.
- **Sales by Category & Sub-Category:** Donut and Bar charts for product distribution.
- **Top 10 Products & Customers:** Tables/Bar charts highlighting top contributors.
- **Sales by Payment & Shipping Mode:** Pie charts analyzing transaction preferences.

## Business Insights
- **Highest Revenue Region:** Identified the region contributing the most to overall revenue.
- **Most Profitable Category:** Highlighted the product category with the highest profit margin.
- **Best-Selling Products:** Uncovered the top 10 products driving sales volume.
- **Monthly Sales Trend:** Detected seasonal peaks in Q4 driven by holiday sales.
- **Customer Purchasing Behavior:** Analyzed segment preferences, with the 'Consumer' segment leading in total orders.

## Future Improvements
- Integrate real-time data using SQL Server or an API.
- Add predictive analytics (e.g., Sales Forecasting) using Python or Power BI's built-in AI visuals.
- Enhance the UI/UX with custom tooltips and dynamic bookmarks.

---

## 🛠️ Step-by-Step Implementation Guide

Follow these steps to recreate this project from scratch:

### Step 1: Generate the Dataset
1. Open your terminal or command prompt (or use VS Code).
2. Navigate to the project folder.
3. Run the provided Python script to generate the 10,000-row dataset:
   ```bash
   python generate_dataset.py
   ```
4. This will create a `sales_data.csv` file inside the `Dataset/` folder.

### Step 2: Import Data into Power BI
1. Open **Microsoft Power BI Desktop**.
2. Click on **Get Data** -> **Text/CSV**.
3. Navigate to the `Dataset/` folder and select `sales_data.csv`.
4. Click **Transform Data** to open the Power Query Editor.

### Step 3: Data Cleaning in Power Query
1. **Remove Duplicates:** Select all columns, right-click the header, and choose *Remove Duplicates*.
2. **Handle Missing Values:** Filter out any null or blank values in critical columns like `Order ID` or `Sales`.
3. **Correct Data Types:** 
   - Ensure `Order Date` and `Ship Date` are set to **Date**.
   - Ensure `Sales`, `Cost`, and `Profit` are set to **Fixed Decimal Number (Currency)**.
   - Ensure `Quantity` is set to **Whole Number**.
4. **Create Date Columns:** 
   - Select the `Order Date` column.
   - Go to the **Add Column** tab -> **Date** -> **Year** -> **Year**.
   - Repeat for **Month** and **Quarter**.
5. Click **Close & Apply** to load the data into Power BI.

### Step 4: Create DAX Measures
Go to the **Model View** or **Report View**, click on **New Measure**, and create the following formulas:

```dax
Total Sales = SUM(sales_data[Sales])

Total Revenue = SUMX(sales_data, sales_data[Quantity] * sales_data[Unit Price] * (1 - sales_data[Discount]))

Total Cost = SUM(sales_data[Cost])

Total Profit = SUM(sales_data[Profit])

Total Orders = DISTINCTCOUNT(sales_data[Order ID])

Average Order Value = DIVIDE([Total Sales], [Total Orders], 0)

Average Sales = AVERAGE(sales_data[Sales])

Profit Margin % = DIVIDE([Total Profit], [Total Sales], 0)

Year-to-Date Sales (YTD) = TOTALYTD([Total Sales], sales_data[Order Date])

Previous Year Sales (PY) = CALCULATE([Total Sales], SAMEPERIODLASTYEAR(sales_data[Order Date]))

Sales Growth % = DIVIDE([Total Sales] - [Previous Year Sales], [Previous Year Sales], 0)
```
*(Note: Create `Running Total`, `Monthly Revenue`, and `Quarterly Revenue` using Quick Measures if needed, or follow similar CALCULATE patterns.)*

### Step 5: Build the Dashboard (Visualizations)

**Design Layout:** Use a modern professional layout with a consistent color palette. Place KPI cards at the top, trend charts in the middle, and breakdown charts at the bottom. Keep slicers on the left side.

#### Page 1: Executive Dashboard
- **KPI Cards:** `Total Sales`, `Total Revenue`, `Total Profit`, `Total Orders`, `Average Order Value`, `Profit Margin %`.
- **Line Chart (Trend):** X-axis: `Order Date` (Month/Year), Y-axis: `Total Sales` & `Total Profit`.
- **Donut Chart:** Legend: `Category`, Values: `Total Sales`.
- **Bar Chart:** X-axis: `Region`, Y-axis: `Total Revenue`.
- **Slicers:** Add slicers for `Year`, `Month`, `Region`, and `Segment` on the left pane.

#### Page 2: Regional Analysis
- **Map Visual:** Location: `State` or `City`, Bubble Size: `Total Sales`, Tooltips: `Total Profit`.
- **Matrix/Table:** Rows: `Region` > `State` > `City`, Values: `Total Sales`, `Total Profit`, `Profit Margin %`.

#### Page 3: Product Analysis
- **Bar Chart:** Top 10 `Product Name` by `Total Sales`.
- **Bar Chart:** Bottom 10 `Product Name` by `Total Sales` (Use Top N filter set to Bottom 10).
- **Scatter Plot:** X-axis: `Total Sales`, Y-axis: `Profit Margin %`, Details: `Sub Category`.

#### Page 4: Customer Analysis
- **Table:** `Customer Name`, `Total Orders`, `Total Sales`. Sort by Sales descending to find Top Customers.
- **Pie Chart:** Legend: `Segment`, Values: `Total Sales`.

### Step 6: Formatting and Publishing
1. **Formatting:** Apply a consistent theme (e.g., **View** -> **Themes**).
2. **Save:** Save your project as `Sales_Dashboard.pbix` in the `Dashboard/` folder.
3. **Publish (Optional):** Click **Publish** on the Home tab to upload your dashboard to the Power BI Service.

## GitHub Repository Instructions
1. Initialize a Git repository in your project folder:
   ```bash
   git init
   ```
2. Create a `.gitignore` file and add `*.pbix` (since Power BI files are binary and can be large):
   ```bash
   echo "*.pbix" > .gitignore
   ```
3. Add your files:
   ```bash
   git add README.md generate_dataset.py Dataset/sales_data.csv Images/dashboard.png
   ```
4. Commit your changes:
   ```bash
   git commit -m "Initial commit: Sales & Revenue Analysis Dashboard"
   ```
5. Push to your GitHub repository and share the link!
