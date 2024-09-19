from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

def customer_clustering(customer_data):
    # Select features for clustering
    features = customer_data[['total_spend', 'quantity', 'invoice_no', 'avg_spend_per_order']]

    # Standardize the data
    scaler = StandardScaler()
    features_scaled = scaler.fit_transform(features)

    # Apply K-Means clustering
    kmeans = KMeans(n_clusters=4, random_state=42)
    customer_data['Cluster'] = kmeans.fit_predict(features_scaled)

    # Visualize clusters using PCA
    pca = PCA(n_components=2)
    pca_components = pca.fit_transform(features_scaled)

    plt.scatter(pca_components[:, 0], pca_components[:, 1], c=customer_data['Cluster'], cmap='viridis')
    plt.title('Customer Segments')
    plt.xlabel('PCA 1')
    plt.ylabel('PCA 2')
    plt.show()

    return customer_data

# Example usage
if __name__ == "__main__":
    import feature_engineering
    customer_data = feature_engineering.create_customer_features(data_loader.load_and_clean_data('customer_shopping_data.csv'))
    customer_clustering(customer_data)
