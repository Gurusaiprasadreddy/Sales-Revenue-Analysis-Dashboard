import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(page_title="Sales & Revenue Dashboard", page_icon="📊", layout="wide")

# Custom CSS for KPI cards
st.markdown("""
<style>
div[data-testid="metric-container"] {
    background-color: #f8f9fa;
    border: 1px solid #dee2e6;
    padding: 5% 5% 5% 10%;
    border-radius: 10px;
    box-shadow: 2px 2px 5px rgba(0,0,0,0.1);
}
</style>
""", unsafe_allow_html=True)

# Load Data
@st.cache_data
def load_data():
    df = pd.read_csv("Dataset/sales_data.csv")
    df['Order Date'] = pd.to_datetime(df['Order Date'])
    df['Month-Year'] = df['Order Date'].dt.to_period('M').astype(str)
    return df

try:
    df = load_data()
except FileNotFoundError:
    st.error("Dataset not found! Please run `python generate_dataset.py` first.")
    st.stop()

# --- Sidebar Filters ---
st.sidebar.header("🔍 Filters")

# Date Filter
min_date = df['Order Date'].min().date()
max_date = df['Order Date'].max().date()
start_date, end_date = st.sidebar.date_input(
    "Select Date Range",
    [min_date, max_date],
    min_value=min_date,
    max_value=max_date
)

# Region Filter
regions = st.sidebar.multiselect(
    "Select Region",
    options=df["Region"].unique(),
    default=df["Region"].unique()
)

# Category Filter
categories = st.sidebar.multiselect(
    "Select Category",
    options=df["Category"].unique(),
    default=df["Category"].unique()
)

# Apply Filters
filtered_df = df[
    (df['Order Date'].dt.date >= start_date) & 
    (df['Order Date'].dt.date <= end_date) &
    (df['Region'].isin(regions)) &
    (df['Category'].isin(categories))
]

st.title("📊 Sales & Revenue Analysis Dashboard")

# --- Top Row: KPIs ---
total_sales = filtered_df['Sales'].sum()
total_profit = filtered_df['Profit'].sum()
total_orders = filtered_df['Order ID'].nunique()
profit_margin = (total_profit / total_sales * 100) if total_sales > 0 else 0

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Sales", f"${total_sales:,.2f}")
col2.metric("Total Profit", f"${total_profit:,.2f}")
col3.metric("Total Orders", f"{total_orders:,}")
col4.metric("Profit Margin %", f"{profit_margin:.2f}%")

st.markdown("---")

# --- Middle Section: Trend & Region ---
col5, col6 = st.columns(2)

with col5:
    st.subheader("Monthly Sales & Profit Trend")
    trend_df = filtered_df.groupby('Month-Year')[['Sales', 'Profit']].sum().reset_index()
    fig_trend = px.line(
        trend_df, x='Month-Year', y=['Sales', 'Profit'], 
        markers=True, 
        color_discrete_map={"Sales": "#1f77b4", "Profit": "#2ca02c"}
    )
    fig_trend.update_layout(xaxis_title="Month", yaxis_title="Amount ($)", legend_title="")
    st.plotly_chart(fig_trend, use_container_width=True)

with col6:
    st.subheader("Revenue by Region")
    region_df = filtered_df.groupby('Region')['Sales'].sum().reset_index()
    fig_region = px.bar(
        region_df, x='Region', y='Sales', 
        text_auto='.2s', 
        color='Sales', color_continuous_scale='Blues'
    )
    st.plotly_chart(fig_region, use_container_width=True)

# --- Lower Section: Products & Category ---
col7, col8 = st.columns(2)

with col7:
    st.subheader("Top 10 Products by Sales")
    top_products = filtered_df.groupby('Product Name')['Sales'].sum().nlargest(10).reset_index()
    fig_products = px.bar(
        top_products, x='Sales', y='Product Name', 
        orientation='h', text_auto='.2s',
        color='Sales', color_continuous_scale='Viridis'
    )
    fig_products.update_layout(yaxis={'categoryorder':'total ascending'})
    st.plotly_chart(fig_products, use_container_width=True)

with col8:
    st.subheader("Sales by Category")
    category_df = filtered_df.groupby('Category')['Sales'].sum().reset_index()
    fig_category = px.pie(
        category_df, names='Category', values='Sales', 
        hole=0.4, color_discrete_sequence=px.colors.qualitative.Pastel
    )
    st.plotly_chart(fig_category, use_container_width=True)

st.markdown("---")
st.caption("Dashboard generated automatically. Data sourced from `sales_data.csv`.")
