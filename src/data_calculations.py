import pandas as pd

def calculate_total_sales(processed_data):
    """
    Calculate total sales price per customer.

    Args:
        processed_data (pandas.DataFrame): Processed sales data.

    Returns:
        pandas.DataFrame: Total sales per customer with customer_id.
    """
    return processed_data.groupby('customer_id')['price'].sum().reset_index()

def calculate_avg_order_quantity(sales_data):
    """
    Calculate the average order quantity per product.

    Args:
        sales_data (pandas.DataFrame): Sales data.

    Returns:
        float: Average order quantity per product.
    """
    return sales_data['quantity'].mean()

def identify_top_selling(products_data, customers_data):
    """
    Identify the top-selling products or customers.

    Args:
        products_data (pandas.DataFrame): Products data.
        customers_data (pandas.DataFrame): Total sales per customer.

    Returns:
        tuple: Top selling products and top customers.
    """
    top_selling_products = products_data.nlargest(3, 'quantity')
    top_customers = customers_data.nlargest(3, 'price')
    return top_selling_products, top_customers

def analyze_sales_trends(sales_data):
    """
    Analyze sales trends over time.

    Args:
        sales_data (pandas.DataFrame): Sales data.

    Returns:
        pandas.Series: Sales trends by month.
    """
    sales_data['date'] = pd.to_datetime(sales_data['order_date'])
    return sales_data.resample('ME', on='date')['price'].sum()
