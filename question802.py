from question8 import user_business, user_business_list_unique

def similarity_knn(dictionary):
    from sklearn.feature_extraction import FeatureHasher
    from sklearn.preprocessing import StandardScaler
    from sklearn.decomposition import PCA
    from sklearn.neighbors import NearestNeighbors
    import numpy as np

    # Use Feature Hasher to reduce dimensionality
    hasher = FeatureHasher(n_features=1000, input_type='string')  # Adjust n_features as needed
    hashed_features = hasher.transform(dictionary.values()).toarray()

    # Apply Z-score normalization
    scaler = StandardScaler()
    user_scaled = scaler.fit_transform(hashed_features)

    # Apply PCA to further reduce dimensionality
    pca = PCA(n_components=20)  # Adjust the number of components as needed
    user_pca = pca.fit_transform(user_scaled)

    # Fit KNN
    knn = NearestNeighbors(n_neighbors=100)
    knn_model = knn.fit(user_pca)

    user_ids = list(dictionary.keys())

    return knn_model, scaler, pca, user_ids


def find_similar_user(knn_model,new_user_data, scaler, pca, user_ids, n_neighbors=10):
    from sklearn.feature_extraction import FeatureHasher
    hasher = FeatureHasher(n_features=1000, input_type='string')
    new_user_hashed = hasher.transform(new_user_data.values()).toarray()
    new_user_scaled = scaler.transform(new_user_hashed)
    new_user_pca = pca.transform(new_user_scaled)

    distances, indices = knn_model.kneighbors(new_user_pca, n_neighbors=n_neighbors)

    return [user_ids[i] for i in indices[0]]




def visualize_knn_clusters(user_pca, user_ids):
    import matplotlib.pyplot as plt
    plt.figure(figsize=(10, 6))

    # Create scatter plot
    plt.scatter(user_pca[:, 0], user_pca[:, 1], c='blue', label='Users')

    # Annotate each point with its user ID
    for i, user_id in enumerate(user_ids):
        plt.annotate(user_id, (user_pca[i, 0], user_pca[i, 1]), fontsize=8, alpha=0.7)

    plt.title('KNN Clusters Visualization')
    plt.xlabel('PCA Feature 1')
    plt.ylabel('PCA Feature 2')
    plt.legend()
    # plt.grid(True)
    plt.savefig("similarity_pca")
    # plt.show()
    return plt.gcf()


if __name__ == "__main__":
    import pandas as pd
    join_review_with_workday = pd.read_csv('join_review_with_workday.csv', low_memory=False)
    user_business_list = user_business(join_review_with_workday)
    unique_user_business = user_business_list_unique(user_business_list)

    # fit a similarity model using KNN and PCA
    similarity_model, scaler, pca, user_ids = similarity_knn(unique_user_business)

    # fine knn for a new user
    new_user_data =list(unique_user_business.items())[10]
    new_user_data ={new_user_data[0]: new_user_data[1]}
    similar_users = find_similar_user(similarity_model,new_user_data, scaler, pca, user_ids, n_neighbors=10)

    # Visualize the PCA components
    from sklearn.feature_extraction import FeatureHasher
    hasher = FeatureHasher(n_features=1000, input_type='string')
    user_pca = pca.transform(scaler.transform(hasher.transform(unique_user_business.values()).toarray()))
    visualize_knn_clusters(user_pca, user_ids)




print("11")