import seaborn as sns
import matplotlib.pyplot as plt

def plot_actual_vs_predicted(y_test, y_pred):
    # Plot actual vs predicted sales
    sns.scatterplot(x=y_test, y=y_pred)
    plt.title('Actual vs Predicted Sales')
    plt.xlabel('Actual Sales')
    plt.ylabel('Predicted Sales')
    plt.show()

def plot_total_spend_by_cluster(customer_data):
    # Visualize total spend by cluster
    sns.boxplot(x='Cluster', y='total_spend', data=customer_data)
    plt.title('Total Spend by Customer Segment')
    plt.show()

# Example usage
if __name__ == "__main__":
    import clustering
    customer_data = clustering.customer_clustering(feature_engineering.create_customer_features(data_loader.load_and_clean_data('customer_shopping_data.csv')))
    plot_total_spend_by_cluster(customer_data)
