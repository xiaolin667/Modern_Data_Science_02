
def word_fre(df, col_names):
    from collections import Counter
    import nltk
    from nltk.corpus import stopwords
    nltk.download('stopwords')

    df[col_names] = df[col_names].astype(str)
    df = df[df[col_names].str.lower() != 'no review']
    all_words = ' '.join(df[col_names]).lower().split()
    # Get English stopwords
    stop_words = set(stopwords.words('english'))
    filtered_words = [word for word in all_words if word.isalpha() and word not in stop_words]

    common_words = Counter(filtered_words).most_common(30)
    return  common_words


def word_fre_per_year(df, col_names):
    from collections import Counter
    import nltk
    from nltk.corpus import stopwords
    nltk.download('stopwords')

    # Ensure that the specified column is of type string
    df[col_names] = df[col_names].astype(str)
    df = df[df[col_names].str.lower() != 'no review']
    df['year'] = pd.to_datetime(df['review_time']).dt.year

    # Get English stopwords
    stop_words = set(stopwords.words('english'))

    # Initialize a dictionary to store the common words per year
    common_words_per_year = {}

    # Group by year and process each group
    for year, group in df.groupby('year'):
        all_words = ' '.join(group[col_names]).lower().split()
        filtered_words = [word for word in all_words if word.isalpha() and word not in stop_words]
        common_words = Counter(filtered_words).most_common(30)
        common_words_per_year[year] = common_words

    return common_words_per_year


def generate_word_clouds(common_words_per_year):
    import matplotlib.pyplot as plt
    from wordcloud import WordCloud
    # Set up the plot with 4 columns and 4 rows
    fig, axes = plt.subplots(nrows=4, ncols=4, figsize=(20, 16))
    axes = axes.flatten()

    # Loop through each year from 2007 to 2021
    for i, year in enumerate(range(2007, 2022)):
        ax = axes[i]

        # Check if the year is in the dictionary
        if year in common_words_per_year:
            words = common_words_per_year[year]

            # Generate a dictionary for the word cloud
            word_freq = {word: count for word, count in words}

            # Create and plot the word cloud
            wordcloud = WordCloud(width=400, height=200, background_color='white').generate_from_frequencies(word_freq)
            ax.imshow(wordcloud, interpolation='bilinear')
            ax.set_title(f"Year: {year}")
            ax.axis('off')  # Turn off axis labels

    # Remove empty subplots if any
    for j in range(i + 1, len(axes)):
        fig.delaxes(axes[j])

    # Adjust layout and show
    plt.tight_layout()
    plt.savefig("word_cloud.png")

    return plt.gcf()

if __name__ == "__main__":
    import pandas as pd
    join_review_with_workday = pd.read_csv('join_review_with_workday.csv',   low_memory=False)
    # common_words =word_fre(join_review_with_workday,'text')

    common_words_per_year = word_fre_per_year(join_review_with_workday,'text')

    word_cloud_per_yea_plots = generate_word_clouds(common_words_per_year)



print("6")