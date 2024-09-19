import data_loader
import feature_engineering
import clustering
import prediction
import visualization
import report_generator

def main():
    # Load and clean the data
    df = data_loader.load_and_clean_data('customer_shopping_data.csv')

    # Feature engineering
    customer_data = feature_engineering.create_customer_features(df)

    # Customer segmentation using clustering
    customer_data = clustering.customer_clustering(customer_data)

    # Predict future sales
    model = prediction.predict_sales(customer_data)

    # Save the results to Excel
    report_generator.save_to_excel(customer_data)

    print("Analysis complete. Report saved.")

if __name__ == "__main__":
    main()
