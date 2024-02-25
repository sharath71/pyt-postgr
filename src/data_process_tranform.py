import pandas as pd

def clean_sales_data(sales_data):
    """
    Perform data cleansing for sales data.

    Args:
        sales_data (pandas.DataFrame): Sales data.

    Returns:
        pandas.DataFrame: Cleaned sales data.
    """
    # Drop rows with missing values
    sales_data.dropna(inplace=True)

    # Convert data types
    sales_data['customer_id'] = sales_data['customer_id'].astype(int)
    sales_data['product_id'] = sales_data['product_id'].astype(int)
    sales_data['order_date'] = pd.to_datetime(sales_data['order_date'])
    sales_data['price'] = sales_data['price'].astype(float)
    sales_data['quantity'] = sales_data['quantity'].astype(int)

    return sales_data

def process_data(sales_data, user_data, fetch_weather_func):
    try:
        # Clean sales data
        sales_data = clean_sales_data(sales_data)

        # Drop rows with missing values
        sales_data.dropna(inplace=True)
        user_data.dropna(inplace=True)

        # Merge sales data with user data
        merged_data = pd.merge(sales_data, user_data, left_on='customer_id', right_on='id')
        merged_data.fillna('', inplace=True)
        merged_data['location'] = merged_data['lat'] + ',' + merged_data['lng']
        merged_data['location'] = merged_data['location'].str.strip()
        
        # Fetch weather data based on location
        merged_data['weather'] = merged_data['location'].apply(fetch_weather_func)
 


        return merged_data

    except Exception as e:
        print(f"Error processing data: {e}")
        return None
