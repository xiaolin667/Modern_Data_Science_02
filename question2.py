from read_in import create_spark, read_data
from question1 import handle_missing, new_time

#1.2.1 calculate the number of reviews per each unique gmap_id
def count_id(dataframe, countby):
    from pyspark.sql.functions import col, count

    df = (
        dataframe
        .groupBy(countby)
        .agg(count(countby).alias(f"count_by_{countby}"))
        .select(col(countby), col(f"count_by_{countby}").cast("float").alias(f"count_by_{countby}"))
    )

    df.orderBy(col(f"count_by_{countby}").desc()).show(5)
    df.write.csv('question2_count_id.csv', header=True)
    return df


def convert_time(time_value):
    import pandas as pd
    if time_value > 1_000_000_000:  # Likely in milliseconds
        seconds_value = time_value / 1000  # Convert to seconds
    else:  # Already in seconds
        seconds_value = time_value

    # Convert to datetime and format as desired
    try:
        return pd.to_datetime(seconds_value, unit='s').strftime('%Y-%m-%d %H')
    except Exception:
        return None  # Handle any conversion failures

# 1.2.2
def review_time(dataframe, columns_name, new_columns):
    import pandas as pd
    dataframe = dataframe.toPandas()
    dataframe[columns_name] = pd.to_numeric(dataframe[columns_name], errors='coerce')
    dataframe = dataframe.dropna(subset=[columns_name])
    dataframe[new_columns] = dataframe[columns_name].apply(convert_time)
    return dataframe

#1.2.3
def plot01(df, columns_name01):
    import matplotlib.pyplot as plt
    import seaborn as sns
    import pandas as pd
    df[columns_name01] = pd.to_datetime(df[columns_name01], format='%Y-%m-%d %H')
    df['hour'] = df[columns_name01].dt.hour
    reviews_by_hour = df.groupby('hour').size().reset_index(name='review_count')

    # Create bins for every 4-hour segment
    bins = [0, 4, 8, 12, 16, 20, 24]
    labels = ['0-4', '4-8', '8-12', '12-16', '16-20', '20-24']
    df['hour_bin'] = pd.cut(df['hour'], bins=bins, labels=labels, right=False)

    #  Create the Line Chart --plot1
    plt.figure(figsize=(8, 6))
    sns.lineplot(data=reviews_by_hour, x='hour', y='review_count', marker='o')
    plt.title('Number of Reviews by Hour')
    plt.xlabel('Hour of Day')
    plt.ylabel('Number of Reviews')
    plt.xticks(range(0, 24))  # Setting X-axis ticks to show each hour
    plt.grid()
    plt.savefig("plot01")

    return plt.gcf()

def plot02(df, columns_name):
    import matplotlib.pyplot as plt
    import seaborn as sns
    import pandas as pd
    df[columns_name] = pd.to_datetime(df[columns_name], format='%Y-%m-%d %H')
    df['hour'] = df[columns_name].dt.hour

    # Create bins for every 4-hour segment
    bins = [0, 4, 8, 12, 16, 20, 24]
    labels = ['0-4', '4-8', '8-12', '12-16', '16-20', '20-24']
    df['hour_bin'] = pd.cut(df['hour'], bins=bins, labels=labels, right=False)

    #  Create the Line Chart --plot2
    reviews_per_bin = df.groupby('hour_bin').size().reset_index(name='review_count')
    plt.figure(figsize=(8, 6))
    sns.barplot(data=reviews_per_bin, x='hour_bin', y='review_count', palette='viridis')
    plt.title('Number of Reviews per 4 Hours')
    plt.xlabel('Hour Bins')
    plt.ylabel('Number of Reviews')
    plt.grid()
    plt.show()
    plt.savefig("plot02")

    return plt.gcf()

def plot03(df, columns_name, group_col):
    import matplotlib.pyplot as plt
    import seaborn as sns
    import pandas as pd

    # Create bins for every 4-hour segment
    bins = [0, 4, 8, 12, 16, 20, 24]
    labels = ['0-4', '4-8', '8-12', '12-16', '16-20', '20-24']
    df['hour_bin'] = pd.cut(df['hour'], bins=bins, labels=labels, right=False)

    df[columns_name] = pd.to_datetime(df[columns_name], format='%Y-%m-%d %H')
    df['hour'] = df[columns_name].dt.hour
    unique_businesses_by_hour = (df.groupby('hour')[group_col].nunique().
                                 reset_index(name='unique_business_count'))
    unique_businesses_by_hour['hour_bin'] = pd.cut(unique_businesses_by_hour['hour'],
                                                   bins=bins, labels=labels,
                                                   right=False)
    # Aggregate by the hour bin, summing the unique counts
    unique_businesses_per_bin = unique_businesses_by_hour.groupby('hour_bin')[
        'unique_business_count'].sum().reset_index()

    # Plot the bar chart
    plt.figure(figsize=(8, 6))
    sns.barplot(data=unique_businesses_per_bin, x='hour_bin',
                y='unique_business_count', palette='viridis')
    plt.title('Number of Unique Businesses Reviewed per 4 Hours')
    plt.xlabel('Hour Bins')
    plt.ylabel('Unique Business Count')
    plt.grid()
    plt.savefig("plot03")

    return  plt.gcf()



if __name__ == "__main__":
    spark = create_spark("review_data")

    review = read_data("/Users/xiaolinsitu/Documents/Deakin/"
             "2_Modern_Data_Science/Assignments/02/review.csv",spark,True,True)

    review , count= handle_missing(review,"text", "no review")
    review = new_time(review, "time", "newtime")

    count_by_gmap_id = count_id(review,"gmap_id")

    review= review_time(review,"time", "review_time")
    print(review.head())

    # plt01 = plot01(review, "review_time")
    # plt01.show()

    plt02 = plot02(review,"review_time")
    # plt02.show()

    plt03 =plot03(review,"review_time","gmap_id")
    # plt03.show()


print("4")