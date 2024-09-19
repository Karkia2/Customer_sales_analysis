def save_to_excel(customer_data, filename='customer_report.xlsx'):
    # Save customer data and clustering to an Excel file
    customer_data.to_excel(filename, index=False)

# Example usage
if __name__ == "__main__":
    import clustering
    customer_data = clustering.customer_clustering(feature_engineering.create_customer_features(data_loader.load_and_clean_data('customer_shopping_data.csv')))
    save_to_excel(customer_data)
