from read_in import create_spark, read_data

def handle_missing(dataframe, columns_name, filled):
    from pyspark.sql.functions import when
    df = dataframe.withColumn(
        columns_name,
        when(dataframe[columns_name].isNull(), filled).otherwise(dataframe[columns_name])
    )

    count = df.filter(df[columns_name] == filled).count()
    return  df ,count

def new_time(dataframe, columns_name, new_column):
    from pyspark.sql import functions as F
    from pyspark.sql.functions import col, from_unixtime
    df_clean = dataframe.withColumn(
        columns_name,
        F.regexp_replace(F.col(columns_name), "[^0-9]", "")
    )
    df_clean = df_clean.dropna(subset=[columns_name])
    df_clean = df_clean.filter(col(columns_name).isNotNull() & (col(columns_name) != ""))
    df_new_time = df_clean.withColumn(
        new_column,
        from_unixtime(col(columns_name).substr(1, 10).cast("long"))
    )
    df_new_time = df_new_time.withColumn(new_column, df_new_time.newtime.cast("date").alias("formatted_time"))
    return df_new_time


if __name__ == "__main__":
    spark = create_spark("review_data")

    review = read_data("/Users/xiaolinsitu/Documents/Deakin/"
             "2_Modern_Data_Science/Assignments/02/review.csv",spark,True,True)

    # question1.1.1 for the none or null in text column, change it to 'no review'
    review , count= handle_missing(review,"text", "no review")
    print(f"Count of 'no review' in 'text' column after handling missing cells: {count}")

    # question 1.1.2 process time column and create new column newtime with format yyyy-mm-dd
    review = new_time(review, "time", "newtime")
    review.show(5)

