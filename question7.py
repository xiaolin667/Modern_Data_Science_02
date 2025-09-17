from question3 import clean_category
import ast

def fre_rating_category(df):

    df['rating'] = pd.to_numeric(df['rating'], errors='coerce')
    filter_df = df[['user_id','gmap_id', 'rating', 'category']].dropna()

    filter_df['new_category'] = filter_df['category'].apply(clean_category).apply(ast.literal_eval)

    df_exploded = filter_df.explode('new_category')
    # merged_df['new_category'] = merged_df['category'].apply(clean_category).apply(ast.literal_eval)
    # Group by category and rating, and count the occurrences
    frequency = df_exploded.groupby(['new_category', 'rating']).size().reset_index(name='frequency')
    # results= frequency.to_dict()

    return frequency

def rating_portion_category(df):
    grouped_df = df.groupby('new_category').apply(
        lambda g: pd.Series({
            'total_frequency': g['frequency'].sum(),
            'portion_of_high_review': g[g['rating'].isin([4, 5])]['frequency'].sum() / g['frequency'].sum(),
            'portion_of_low_review': g[g['rating'].isin([1, 2, 3])]['frequency'].sum() / g['frequency'].sum()
        })
    ).reset_index()

    # Filtering categories with a total frequency greater than 5
    result_df = grouped_df[grouped_df['total_frequency'] > 5]

    return result_df

def plot_portion_rating_category(df):
    import pandas as pd
    import matplotlib.pyplot as plt
    df = df[df['total_frequency'] >=2000]
    plt.figure(figsize=(10, 6))
    plt.scatter(df['total_frequency'], df['portion_of_high_review'], color='blue')
    plt.title('Scatterplot of Total Frequency vs Portion of High Review')
    plt.xlabel('Total Frequency')
    plt.ylabel('Portion of High Review')
    plt.grid(True)

    plt.savefig("portion_rating_category_over2000")
    # plt.show()

    return plt.gcf()

def review_of_low_rating_category(df1, df2):
    # Step 1: Filter categories with portion_of_low_review > 0.3
    filtered_portion = df1[df1['portion_of_low_review'] > 0.6]
    df2 = df2[['text', 'category']].dropna()

    df2['new_category'] = df2['category'].apply(clean_category).apply(ast.literal_eval)
    exploded_reviews = df2.explode('new_category')

    # Map the data
    filtered_data = exploded_reviews[exploded_reviews['new_category'].isin(filtered_portion['new_category'])]

    # Select and print/return only required columns
    result = filtered_data[['text', 'new_category']]
    return result

def low_review_cloud(df):
    import matplotlib.pyplot as plt
    from wordcloud import WordCloud
    import pandas as pd

    df = df[df['text'] != 'no review']
    categories = df['new_category'].unique()

    # Initialize subplot
    num_plots = len(categories)
    num_cols = 2
    num_rows = (num_plots // num_cols) + (num_plots % num_cols > 0)

    fig, ax = plt.subplots(1, len(categories), figsize=(15, 7))

    # Generate word cloud for each category
    for i, category in enumerate(categories):
        text = " ".join(df[df['new_category'] == category]['text'])
        wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)

        ax[i].imshow(wordcloud, interpolation='bilinear')
        ax[i].set_title(category)
        ax[i].axis('off')
    plt.savefig("low_review_cloud_category.png")

    return  plt.gcf()




if __name__ == "__main__":
    # 1.7.1 frequency of ratings for each category
    import pandas as pd
    join_review_with_workday = pd.read_csv('join_review_with_workday.csv', low_memory=False)
    fre_rating_category = fre_rating_category(join_review_with_workday)

    # portion of high/low ratings for each category
    portion_rating_category = rating_portion_category(fre_rating_category)
    plot_portion_rating_rate =plot_portion_rating_category(portion_rating_category)

    #1.7.2 categories with low ratings
    low_rating_review = review_of_low_rating_category(portion_rating_category, join_review_with_workday)
    low_review_cloud_category = low_review_cloud(low_rating_review)



print("9")