
import matplotlib.pyplot as plt
import re

def clean(df):  #drop unnecessary columns and remove duplicate
    #drop
    columns_to_drop = ['time', 'pics', 'resp', 'description', 'latitude', 'longitude',
                       'num_of_reviews', 'MISC', 'state', 'relative_results', 'url']
    df = df.drop(columns=columns_to_drop)

    # remove duplicate by 'user_id', 'gmap_id', 'review_time'
    df = df.drop_duplicates(subset=['user_id', 'gmap_id', 'review_time'])

    return df

def work_day(df, col_name, new_col):
    df[col_name] = pd.to_datetime(df[col_name], errors='coerce', format='%Y-%m-%d')
    # Day of the week mapping
    map = {
        1: "Sunday",
        2: "Monday",
        3: "Tuesday",
        4: "Wednesday",
        5: "Thursday",
        6: "Friday",
        7: "Saturday"
    }
    df[new_col] = df[col_name].dt.dayofweek.map(map)

    return df

#1.3.1
def average_records_per_weekday(df, col_name1, col_name2):  #col_name1 = newtime, col_name2 = work_day
    # Group by 'newtime' and 'work_day' to count occurrences
    grouped = df.groupby([col_name1, col_name2]).size().reset_index(name='counts')
    average_counts = grouped.groupby(col_name2)['counts'].mean()

    return average_counts

def avg_workday_plot(avg_review_per_workday, filename):
    # Define the order of weekdays
    weekday_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    average_records = avg_review_per_workday.reindex(weekday_order)

    plt.figure(figsize=(8, 5))
    average_records.plot(kind='line', marker='o')

    plt.title('Average Number of Records per Work Day')
    plt.xlabel('Work Day')
    plt.ylabel('Average Count')
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(filename)
    return plt.gcf()


def detect_and_escape_apostrophe(text):
    """
    Detect possessive plural words ending with single quote and escape them.
    Returns a tuple with (detected_words, escaped_text)
    """
    # Pattern to detect words ending with single quote followed by space
    pattern = r"\b(\w+)'(\s)"

    # Find all matches
    matches = re.findall(pattern, text)
    detected_words = [f"{word}'" for word, space in matches]

    # Escape the single quotes by replacing ' with \'
    escaped_text = re.sub(pattern, r"\1\\'\2", text)

    return escaped_text


def clean_category(category_str):
    import ast
    pass_flag = True
    try:
        ast.literal_eval(category_str)
    except SyntaxError:
        pass_flag = False
    except ValueError:
        return ''
    except TypeError:
        return ''
    if pass_flag:
        return category_str
    category_str = str(category_str)
    clean_str = (category_str.replace('""', '"').
                 replace('"', "'").replace("'[", "["))
    # Escape single quotes within strings
    clean_str = clean_str.replace("''", "'")  # .replace("\\'", "'")
    pattern = r"'\b[a-z]"

    # Replace single quotes with escaped single quotes
    clean_str = detect_and_escape_apostrophe(re.sub(pattern, r"\'", clean_str))

    # Ensure the string ends with a closing bracket
    if not clean_str.endswith(']'):
        clean_str += ']'
    return clean_str

def business_highest_rating(df, best_day):
    import ast
    import pandas as pd
    from wordcloud import WordCloud
    import matplotlib.pyplot as plt

    best_day_reviews = df[df['work_day'] == best_day]

    #drop invalid rows and convert "rating" to numeric
    valid_ratings = best_day_reviews['rating'].isin(["1", "2", "3", "4", "5"])
    valid_df = best_day_reviews[valid_ratings]
    best_day_reviews['rating'] = pd.to_numeric(valid_df['rating'], errors='coerce')

    # groupby
    average_ratings = best_day_reviews.groupby('gmap_id')['rating'].mean()
    max_avg_rating = average_ratings.max()
    highest_avg_rating_ids = average_ratings[average_ratings == max_avg_rating].index
    business_names = []
    all_categories = []

    for gmap_id in highest_avg_rating_ids:
        business_info = df[df['gmap_id'] == gmap_id].iloc[0]
        business_names.append(business_info['name_y'])

        try:
            # Safely evaluate the new_category field
            categories = ast.literal_eval(clean_category(business_info['new_category']))
            all_categories.extend(categories)
        except (ValueError, SyntaxError):
            # Handle any parsing errors gracefully
            pass
    # Remove duplicates from categories
    all_categories = list(set(all_categories))

    # Create a word cloud for business names
    wordcloud_names = WordCloud(width=800, height=400, background_color='white').generate(' '.join(business_names))

    # Create a word cloud for categories
    wordcloud_categories = WordCloud(width=800, height=400, background_color='white').generate(' '.join(all_categories))

    # Display word cloud for business names
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud_names, interpolation='bilinear')
    plt.axis('off')  # Turn off the axis
    plt.title(f'Business Names with highest averaged ratings at {best_day}')
    plt.savefig(f"Business Names with highest averaged ratings at {best_day}")

    # Display word cloud for categories
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud_categories, interpolation='bilinear')
    plt.axis('off')  # Turn off the axis
    plt.title(f'Categories with highest averaged ratings at {best_day}')
    plt.savefig(f"Categories with highest averaged ratings at {best_day}")
    return  plt.gcf()

def plot_rating_fre(df, best_day):
    import ast
    import pandas as pd

    best_day_reviews = df[df['work_day'] == best_day]

    #drop invalid rows and convert "rating" to numeric
    valid_ratings = best_day_reviews['rating'].isin(["1", "2", "3", "4", "5"])
    valid_df = best_day_reviews[valid_ratings]
    best_day_reviews['rating'] = pd.to_numeric(valid_df['rating'], errors='coerce')
    rating_counts = best_day_reviews['rating'].value_counts().sort_index()

    plt.figure(figsize=(10, 6))
    rating_counts.plot(kind='bar', color='skyblue')
    plt.title(f'Frequency of Ratings on {best_day}')
    plt.xlabel('Rating')
    plt.ylabel('Frequency')
    plt.xticks(rotation=0)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.savefig(f"rating_frequency_{best_day}.png")

    return plt.gcf()

def plot_rating_fre_pie(df, best_day):
    best_day_reviews = df[df['work_day'] == best_day]

    # Drop invalid rows and convert "rating" to numeric
    valid_ratings = best_day_reviews['rating'].isin(["1", "2", "3", "4", "5"])
    valid_df = best_day_reviews[valid_ratings]
    valid_df['rating'] = pd.to_numeric(valid_df['rating'], errors='coerce')
    rating_counts = valid_df['rating'].value_counts().sort_index()

    # Plotting a pie chart with percentages
    plt.figure(figsize=(8, 8))
    plt.pie(
        rating_counts,
        labels=rating_counts.index,
        autopct='%1.1f%%',
        startangle=90,
        colors=plt.cm.tab20.colors
    )
    plt.title(f'Percentage of Ratings on {best_day}')
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.savefig(f"rating_percentage_{best_day}.png")

    return plt.gcf()


if __name__ == "__main__":
    import pandas as pd
    # 1.3.1 cal the average
    join_review_with_workday = pd.read_csv('join_review_with_workday.csv')
    avg_review_per_workday = average_records_per_weekday(join_review_with_workday,"newtime", "work_day")
    avg_workday_plot = avg_workday_plot(avg_review_per_workday,'average_review_workday.png')

    # 1.3.2
    #clean category first
    join_review_with_workday['new_category'] = join_review_with_workday['category'].apply(clean_category)
    best_day = avg_review_per_workday.idxmax()
    best_rating_business_categories = business_highest_rating(join_review_with_workday, best_day)

    #1.3.3
    #explore the data on name of business
    # how likely the business can get a good rating in friday?
    plot_rating_fre = plot_rating_fre(join_review_with_workday, best_day)
    plot_rating_fre_pie = plot_rating_fre_pie(join_review_with_workday, best_day)
#
#     # best_day = 'Monday'
#     # plot_rating_fre_monday = plot_rating_fre(join_review_with_workday, best_day)
#     # plot_rating_fre_pie_monday =plot_rating_fre_pie(join_review_with_workday, best_day)
#
#
# print("5")