import csv
import pandas as pd
import fetch_source_data
import data_process_tranform
import data_calculations


def main():
    # Fetch user data from JSONPlaceholder API
    user_data = fetch_source_data.fetch_user_data()
    
    # Load sales data from CSV file
    sales_data = pd.read_csv('src/sales_data.csv')

    # Process data
    #processed_data = data_process_tranform.process_data(sales_data, user_data, fetch_source_data.fetch_weather_func)
    
    processed_data = pd.read_csv('datastore.csv')
    # Calculate total sales amount per customer
    total_sales = data_calculations.calculate_total_sales(processed_data)
    total_sales.to_csv('total_sales_csv',index=False)

    # Calculate average order quantity per product
    avg_order_quantity = data_calculations.calculate_avg_order_quantity(sales_data)
    print(avg_order_quantity)

    # Identify top selling products and customers
    top_selling_products, top_customers = data_calculations.identify_top_selling(processed_data, total_sales)
    top_selling_products.to_csv('top_selling_products.csv',index=False)
    top_customers.to_csv('top_customers.csv',index=False)

    # Analyze sales trends over time
    sales_trends = data_calculations.analyze_sales_trends(processed_data)

    # Store transformed data in database
    # data_store.store_data_in_database(processed_data)

    # Print or visualize insights (not implemented in this code snippet)
    print(processed_data)
    print("Pipeline completed successfully!")

if __name__ == "__main__":
    main()
