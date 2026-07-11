import csv
import random
from datetime import datetime, timedelta
import os

def generate_data():
    records = []
    
    segments = ['Consumer', 'Corporate', 'Home Office']
    countries = ['United States', 'Canada', 'United Kingdom', 'Australia', 'Germany', 'France']
    regions = ['North', 'South', 'East', 'West', 'Central']
    categories = ['Furniture', 'Office Supplies', 'Technology']
    
    sub_categories = {
        'Furniture': ['Bookcases', 'Chairs', 'Labels', 'Tables', 'Furnishings'],
        'Office Supplies': ['Appliances', 'Art', 'Binders', 'Envelopes', 'Fasteners', 'Paper', 'Storage', 'Supplies'],
        'Technology': ['Accessories', 'Copiers', 'Machines', 'Phones']
    }
    
    payment_modes = ['Credit Card', 'Debit Card', 'PayPal', 'Bank Transfer', 'Cash on Delivery']
    shipping_modes = ['Standard Class', 'Second Class', 'First Class', 'Same Day']

    start_date = datetime(2023, 1, 1)
    
    print("Generating 10000 records...")
    for i in range(1, 10001):
        order_id = f"ORD-{20230000 + i}"
        days_offset = random.randint(0, 1095) # 3 years
        order_date = start_date + timedelta(days=days_offset)
        ship_offset = random.randint(1, 7)
        ship_date = order_date + timedelta(days=ship_offset)
        
        customer_id = f"CUST-{random.randint(1000, 9999)}"
        customer_name = f"Customer {customer_id.split('-')[1]}"
        segment = random.choice(segments)
        country = random.choice(countries)
        state = f"State_{random.randint(1, 50)}"
        city = f"City_{random.randint(1, 100)}"
        region = random.choice(regions)
        
        category = random.choice(categories)
        sub_category = random.choice(sub_categories[category])
        product_id = f"PROD-{category[:3].upper()}-{random.randint(1000, 9999)}"
        product_name = f"{sub_category} Product {random.randint(1, 50)}"
        
        quantity = random.randint(1, 15)
        unit_price = round(random.uniform(5.0, 500.0), 2)
        discount = round(random.uniform(0.0, 0.3), 2)
        
        sales = round((quantity * unit_price) * (1 - discount), 2)
        cost_multiplier = random.uniform(0.4, 0.8)
        cost = round(sales * cost_multiplier, 2)
        profit = round(sales - cost, 2)
        profit_margin = round(profit / sales, 4) if sales > 0 else 0
        
        payment_mode = random.choice(payment_modes)
        shipping_mode = random.choice(shipping_modes)
        
        records.append([
            order_id, order_date.strftime("%Y-%m-%d"), ship_date.strftime("%Y-%m-%d"),
            customer_id, customer_name, segment, country, state, city, region,
            product_id, category, sub_category, product_name, quantity, unit_price,
            discount, sales, cost, profit, profit_margin, payment_mode, shipping_mode
        ])

    print("Writing to CSV...")
    os.makedirs('Dataset', exist_ok=True)
    os.makedirs('Dashboard', exist_ok=True)
    os.makedirs('Images', exist_ok=True)

    with open('Dataset/sales_data.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow([
            "Order ID", "Order Date", "Ship Date", "Customer ID", "Customer Name", 
            "Segment", "Country", "State", "City", "Region", "Product ID", 
            "Category", "Sub Category", "Product Name", "Quantity", "Unit Price", 
            "Discount", "Sales", "Cost", "Profit", "Profit Margin", 
            "Payment Mode", "Shipping Mode"
        ])
        writer.writerows(records)
    print("Done!")

if __name__ == "__main__":
    generate_data()
