import pandas
from question3 import clean_category

# Function to calculate the number of unique reviewers for each business
def count_unique_reviewers_business(df):
    unique_reviewers_business = df.groupby('gmap_id')['user_id'].nunique().reset_index()
    unique_reviewers_business.columns = ['gmap_id', 'unique_reviewer_count']
    return unique_reviewers_business

# Function to find the business with the most unique reviewers
def business_with_most_reviewers(df, top_num):
    unique_reviewers = count_unique_reviewers_business(df)
    top_businesses_most_reviewers = unique_reviewers.nlargest(top_num, 'unique_reviewer_count')
    # max_reviewers = unique_reviewers['unique_reviewer_count'].max()
    # top_businesses_most_reviewers = unique_reviewers[unique_reviewers['unique_reviewer_count'] == max_reviewers]
    return top_businesses_most_reviewers

def plot_business_most_reviewers_top10(df_unique):
    import matplotlib.pyplot as plt
    import numpy as np
    import pandas as pd
    # Read the CSV file into a DataFrame
    df_count = pd.read_csv('question2_count_id.csv', delimiter=';')
    df_merged = pd.merge(df_unique, df_count, on='gmap_id', how='inner')
    plt.figure(figsize=(12, 6))

    # Set the position for each bar
    bar_width = 0.35
    index = np.arange(len(df_merged))

    # Create bars for unique_reviewer_count
    plt.bar(index, df_merged['unique_reviewer_count'], bar_width, label='Unique Reviewer Count', color='b')

    # Create bars for count_id, offset to the right
    plt.bar(index + bar_width, df_merged['count_id'], bar_width, label='Count ID', color='r')

    # Add labels, title, and legend
    plt.xlabel('gmap_id', fontweight='bold')
    plt.ylabel('Count', fontweight='bold')
    plt.title('Unique Reviewer Count vs Count ID')
    plt.xticks(index + bar_width / 2, df_merged['gmap_id'], rotation=45)
    plt.legend()

    # Show the plot
    plt.tight_layout()
    plt.savefig("plot_business_most_reviewer_top10.png")
    return plt.gcf()


def handle_unmatched_brackets_in_category(df: pandas.DataFrame):
    # Function to add a backslash before a single quote
    def escape_quotes(s):
        if 'Bridal' in s:
            print("stop here.")
        return "'" + s.strip("''").replace("'", "\\'") + "'"
    # Apply the function to the 'category' column, only on the content within brackets
    df['new_category'] = df['new_category'].apply(
        lambda x: '[' + ', '.join(escape_quotes(elem.strip()) for elem in x.strip('[]').split(', ')) + ']'
    )
    return df

# Function to extract and count unique reviewers per category
def find_top_categories(df,  top_n=10):
    import ast
    merged_df = join_review_with_workday.merge(df, on='gmap_id')
    merged_df = merged_df[['user_id', 'category']].dropna()
    merged_df['new_category'] = merged_df['category'].apply(clean_category).apply(ast.literal_eval)
    exploded_df = merged_df.explode('new_category')
    unique_counts = exploded_df.groupby('new_category')['user_id'].nunique()
    result = unique_counts.to_dict()

    return  result

def temporal_pattern(df):
    import matplotlib.pyplot as plt
    # 1. Convert "review_time" to time format
    df['review_time'] = pd.to_datetime(df['review_time'], errors='coerce')

    # 2. Drop rows where "review_time" is na, missing, or NaN
    df = df.dropna(subset=['review_time'])

    # 3. Count total reviews (rows) of each year "review_year"
    df['review_year'] = df['review_time'].dt.year
    yearly_counts = df['review_year'].value_counts().sort_index()

    # 4. Count total reviews (rows) of each month "review_month"
    df['review_month'] = df['review_time'].dt.month
    monthly_counts = df['review_month'].value_counts().sort_index()

    # 5. Count total reviews (rows) of each day "review_day"
    df['review_day'] = df['review_time'].dt.day
    daily_counts = df['review_day'].value_counts().sort_index()

    # 6. Count total reviews (rows) of each hour of a day "review_hour"
    df['review_hour'] = df['review_time'].dt.hour
    hourly_counts = df['review_hour'].value_counts().sort_index()

    # Create subplots
    fig, axs = plt.subplots(2, 2, figsize=(14, 8))

    # Plot Yearly Reviews
    axs[0, 0].plot(yearly_counts.index, yearly_counts.values, label='Yearly Reviews', color='b')
    axs[0, 0].set_title('Yearly Reviews')
    axs[0, 0].set_xlabel('Year')
    axs[0, 0].set_ylabel('Number of Reviews')
    axs[0, 0].grid(True)

    # Plot Monthly Reviews
    axs[0, 1].plot(monthly_counts.index, monthly_counts.values, label='Monthly Reviews', color='r')
    axs[0, 1].set_title('Monthly Reviews')
    axs[0, 1].set_xlabel('Month')
    axs[0, 1].set_ylabel('Number of Reviews')
    axs[0, 1].grid(True)

    # Plot Daily Reviews
    axs[1, 0].plot(daily_counts.index, daily_counts.values, label='Daily Reviews', color='g')
    axs[1, 0].set_title('Daily Reviews')
    axs[1, 0].set_xlabel('Day')
    axs[1, 0].set_ylabel('Number of Reviews')
    axs[1, 0].grid(True)

    # Plot Hourly Reviews
    axs[1, 1].plot(hourly_counts.index, hourly_counts.values, label='Hourly Reviews', color='m')
    axs[1, 1].set_title('Hourly Reviews')
    axs[1, 1].set_xlabel('Hour')
    axs[1, 1].set_ylabel('Number of Reviews')
    axs[1, 1].grid(True)

    # Tight layout for subplots
    plt.tight_layout()
    plt.savefig("temporal_patterns")
    # plt.show()

    return yearly_counts, monthly_counts, daily_counts, hourly_counts


if __name__ == "__main__":
    import pandas as pd
    from question2 import count_id
    #1.5.1
    join_review_with_workday = pd.read_csv('join_review_with_workday.csv',   low_memory=False)
    unique_reviewers_business = count_unique_reviewers_business(join_review_with_workday)
    top_businesses_most_reviewers = business_with_most_reviewers(join_review_with_workday, 10)
    # plot = plot_business_most_reviewers_top10(top_businesses_most_reviewers)



    # find the top 10 categories with most unique reviewers using top 1000 business
    top_1000_businesses_most_reviewers =business_with_most_reviewers(join_review_with_workday, 1000)
    top_categories = find_top_categories(top_1000_businesses_most_reviewers, 10)
    sorted_by_keys = sorted(top_categories.items(),  key=lambda item: item[1], reverse=True)
    top_10 = dict(sorted_by_keys[:10])

    yearly_counts, monthly_counts, daily_counts, hourly_counts = temporal_pattern(join_review_with_workday)



print("7")