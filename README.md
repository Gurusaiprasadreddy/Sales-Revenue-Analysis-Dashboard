# 📊 Sales & Revenue Analysis Dashboard (Python)

## Project Overview
This project is an end-to-end Data Analytics portfolio project designed to analyze sales performance, revenue trends, customer behavior, and profitability. Originally envisioned for Power BI, this dashboard has been fully developed using **Python and Streamlit**, delivering a highly interactive, web-based experience. It empowers stakeholders with actionable insights to drive data-driven decision-making.

## 🚀 Features
- **Executive Dashboard:** High-level KPIs including Total Sales, Total Profit, and Profit Margin.
- **Interactive Slicers:** Dynamic sidebar filtering by Date Range, Region, and Product Category.
- **Trend Analysis:** Monthly Sales & Profit line charts to identify seasonality.
- **Geographical Breakdown:** Revenue by Region visualization.
- **Product Deep Dive:** Top 10 Products by Sales and Sales by Category breakdowns.

## 🛠️ Tech Stack
- **Python:** Core programming language.
- **Streamlit:** For building the interactive web application UI.
- **Pandas:** For data manipulation and aggregation.
- **Plotly Express:** For generating beautiful, interactive charts.

## 📂 Project Structure
```text
Sales-Revenue-Dashboard/
│── Dataset/
│     sales_data.csv        # 10,000-row realistic sales dataset
│── app.py                  # Main Streamlit dashboard application
│── generate_dataset.py     # Script to generate the dataset
│── .gitignore              # Git ignore file
└── README.md               # Project documentation
```

## ⚙️ How to Run Locally

Follow these steps to run the dashboard on your own machine:

### 1. Generate the Dataset
Run the data generation script to create the 10,000-row `sales_data.csv` file:
```bash
python generate_dataset.py
```

### 2. Install Dependencies
Install the required Python libraries using pip:
```bash
pip install streamlit pandas plotly
```

### 3. Launch the Dashboard
Run the Streamlit application using the python module flag:
```bash
python -m streamlit run app.py
```
*Your default web browser will automatically open a new tab pointing to `http://localhost:8501` where you can interact with the dashboard.*

## 📈 Key Performance Indicators (KPIs)
- **Total Sales:** Overall sales value generated.
- **Total Profit:** Overall profit achieved after costs.
- **Total Orders:** Count of unique orders processed.
- **Profit Margin %:** Profit as a percentage of total sales.

## 💡 Business Insights
- **Seasonality:** Trend charts reveal distinct peaks in Q4 driven by holiday sales.
- **Top Performers:** A small subset of products drives the vast majority of sales volume.
- **Regional Strength:** Certain regions significantly outperform others, indicating potential areas for expansion or marketing reallocation.

## 🔗 GitHub Instructions
To push this project to your GitHub repository:
```bash
git init
git add .
git commit -m "Initial commit: Python Streamlit Sales Dashboard"
git branch -M main
git remote add origin https://github.com/Gurusaiprasadreddy/Sales-Revenue-Analysis-Dashboard.git
git push -u origin main
```
