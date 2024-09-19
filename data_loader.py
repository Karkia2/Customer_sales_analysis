import pandas as pd

def load_and_clean_data(file_path):
    # Load the dataset
    df = pd.read_csv(file_path)

    # Convert invoice_date to datetime with dayfirst=True
    df['invoice_date'] = pd.to_datetime(df['invoice_date'], dayfirst=True)

    # Create a new total_spend column
    df['total_spend'] = df['price'] * df['quantity']

    # Drop rows with missing values
    df = df.dropna()

    return df

# Example usage
if __name__ == "__main__":
    data = load_and_clean_data('customer_shopping_data.csv')
    print(data.head())
