
def recommend_business(df, user_id, num_recommendations=5):
    import pandas as pd
    import numpy as np
    from scipy.sparse.linalg import svds
    df['rating'] = pd.to_numeric(df['rating'], errors='coerce')
    # Create user-item matrix
    user_item_matrix = df.pivot_table(index='user_id', columns='gmap_id', values='rating').fillna(0)

    # Normalize the matrix by subtracting the mean rating for each user
    user_ratings_mean = np.mean(user_item_matrix.values, axis=1)
    user_item_matrix_demeaned = user_item_matrix.values - user_ratings_mean.reshape(-1, 1)

    # Perform matrix factorization using SVD
    U, sigma, Vt = svds(user_item_matrix_demeaned, k=50)
    sigma = np.diag(sigma)

    # Reconstruct the matrix
    all_user_predicted_ratings = np.dot(np.dot(U, sigma), Vt) + user_ratings_mean.reshape(-1, 1)

    # Convert to DataFrame for easy handling
    preds_df = pd.DataFrame(all_user_predicted_ratings, columns=user_item_matrix.columns, index=user_item_matrix.index)

    # Recommend businesses
    user_row_number = user_item_matrix.index.get_loc(user_id)
    sorted_user_predictions = preds_df.iloc[user_row_number].sort_values(ascending=False)

    # Get the user's data and merge with the recommendations
    user_data = df[df.user_id == user_id]
    recommendations = df[~df['gmap_id'].isin(user_data['gmap_id'])]
    recommendations = recommendations.merge(sorted_user_predictions.reset_index(), on='gmap_id')
    recommendations.rename(columns={recommendations.columns[-1]: 'predicted_rating'}, inplace=True)
    # recommendations = recommendations.rename(columns={user_row_number: 'predicted_rating'})

    # Recommend the top 'num_recommendations' businesses
    final_recommendations = recommendations.sort_values('predicted_rating', ascending=False).drop_duplicates(
        'gmap_id').head(num_recommendations)

    # Format the output
    final_recommendations = final_recommendations[['name_y', 'predicted_rating', 'category']]
    final_recommendations = final_recommendations.rename(columns={'name_y': 'name', 'category': 'categories'})

    return final_recommendations

if __name__ == "__main__":
    import pandas as pd
    join_review_with_workday = pd.read_csv('join_review_with_workday.csv', low_memory=False)

    user_id =join_review_with_workday['user_id'].sample(n=1).iloc[0]
    recommended_businesses = recommend_business(join_review_with_workday, user_id, num_recommendations=5)

print("8")