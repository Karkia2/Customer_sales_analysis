def create_customer_features(df):
    # Group by customer_id to create customer-level features
    customer_data = df.groupby('customer_id').agg({
        'total_spend': 'sum',      # Total spend by the customer
        'quantity': 'sum',         # Total quantity purchased
        'invoice_no': 'nunique',   # Number of unique transactions (invoices)
        'age': 'mean',             # Average age of the customer
        'gender': 'first'          # Gender of the customer
    }).reset_index()

    # Calculate the average spend per transaction
    customer_data['avg_spend_per_order'] = customer_data['total_spend'] / customer_data['invoice_no']

    return customer_data

# Example usage
if __name__ == "__main__":
    import data_loader
    df = data_loader.load_and_clean_data('customer_shopping_data.csv')
    customer_data = create_customer_features(df)
    print(customer_data.head())
