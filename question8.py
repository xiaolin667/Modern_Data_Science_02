from itertools import combinations
import pickle
from scipy.sparse import csr_matrix
from itertools import combinations
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np


def user_business(df):
    user_business_list = {}
    for user_id, group in df.groupby('user_id'):
        sorted_group = group.sort_values('newtime')
        business_names = sorted_group['name_y'].tolist()
        user_business_list[user_id] = business_names

    return user_business_list

def user_business_list_unique(dictionary):
    # Create a new dictionary to store unique businesses
    unique_user_business = {}

    # Iterate over the dictionary to check duplicates and remove them
    for user_id, businesses in dictionary.items():
        # Find unique businesses
        unique_businesses = list(set(businesses))
        unique_user_business[user_id] = unique_businesses

        # Task 1: Print number of elements and check duplicates for top 100 user_id
    print("Task 1: Check for duplicates")
    for user_id in list(dictionary.keys())[:200]:
        original_count = len(dictionary[user_id])
        unique_count = len(set(dictionary[user_id]))
        has_duplicates = 'Y' if original_count != unique_count else 'N'

        print(f"User ID: {user_id}, Number of Elements: {original_count}, Duplicates: {has_duplicates}")

    # Task 3: Print number of elements and how many were removed for top 100 user_id
    print("\nTask 3: After removing duplicates")

    for user_id in list(dictionary.keys())[:200]:
        original_count = len(dictionary[user_id])
        unique_count = len(dictionary[user_id])
        duplicates_removed = original_count - unique_count

        print(
            f"User ID: {user_id}, "
            f"Number of Elements: {original_count}, "
            f"Number of Unique Elements: {unique_count}, "
            f"Duplicates Removed: {duplicates_removed}"
        )
    return unique_user_business


from sklearn.preprocessing import LabelEncoder
from itertools import combinations
import numpy as np


def encode_businesses(user_business_dict):
    # Flatten the list of business names
    all_businesses = [business for businesses in user_business_dict.values() for business in businesses]

    # Initialize and fit the label encoder
    le = LabelEncoder()
    le.fit(all_businesses)

    # Encode the businesses for each user
    encoded_user_business_dict = {}

    for user_id, businesses in user_business_dict.items():
        encoded_user_business_dict[user_id] = set(le.transform(businesses))

    return encoded_user_business_dict


if __name__ == "__main__":
    #1.8.1 reviewer_business_list
    import pandas as pd
    join_review_with_workday = pd.read_csv('join_review_with_workday.csv', low_memory=False)
    user_business_list = user_business(join_review_with_workday)

    #1.8.2 remove duplicated pairs
    unique_user_business = user_business_list_unique(user_business_list)

    # 1.8.3 jaccard user similarity, total 20000 users
    # users_similarities =compute_jaccard_similarities(unique_user_business)

    # users_similarities =compute_jaccard_similarities_decom(unique_user_business)
    # save_similarities(users_similarities, 'user_similarities.pkl')
    #
    # # Example usage: load the saved similarities
    # similarities = load_similarities('user_similarities.pkl')



print("10")

