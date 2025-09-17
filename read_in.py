
def create_spark(session_name):
    # import spark
    from pyspark.sql import SparkSession
    spark = SparkSession.builder \
        .appName(session_name) \
        .getOrCreate()
    return spark

def read_data(link, spark, header =True, inferSchema=True ):
    df = spark.read.csv(link, header=True, inferSchema=True)
    return df

def data_inspect(dataframe):
    dataframe.show(5)
    dataframe.printSchema()
    rows = dataframe.count()
    columns = len(dataframe.columns)
    print(f"This dataframe contains: {rows} rows and {columns} columns.")

def check_missing(dataframe):
    from pyspark.sql import functions as F
    missing_values = dataframe.select(
        [((dataframe[col].isNull()).cast("int").alias(col)) for col in dataframe.columns])
    missing_sum = missing_values.agg(*[(F.sum(col).alias(col)) for col in dataframe.columns]).collect()[0]
    print(f"Missing values in {dataframe}:")
    for cols in dataframe.columns:
        print(f"{cols}: {missing_sum[cols]}")


if __name__ == "__main__":
    spark = create_spark("review_data")

    review = read_data("/Users/xiaolinsitu/Documents/Deakin/"
             "2_Modern_Data_Science/Assignments/02/review.csv",spark,True,True)
    data_inspect(review)
    check_missing(review)

    meta_review_business = read_data("/Users/xiaolinsitu/Documents/Deakin/"
             "2_Modern_Data_Science/Assignments/02/meta-review-business.csv",spark,True,
                                     True)
    data_inspect(meta_review_business)
    check_missing(meta_review_business)


