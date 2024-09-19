from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

def predict_sales(customer_data):
    # Define features and target for prediction
    X = customer_data[['invoice_no', 'quantity', 'avg_spend_per_order']]
    y = customer_data['total_spend']

    # Split into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train the Random Forest model
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Make predictions and evaluate the model
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    print(f'Mean Squared Error: {mse}')
    print(f'R-squared: {r2}')

    return model

# Example usage
if __name__ == "__main__":
    import feature_engineering
    customer_data = feature_engineering.create_customer_features(data_loader.load_and_clean_data('customer_shopping_data.csv'))
    predict_sales(customer_data)
