import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose


def process_reviews(df):
    df['newtime'] = pd.to_datetime(df['newtime'])
    df = df[(df['newtime'] >= '2016-01-01') & (df['newtime'] <= '2025-09-30')]

    daily_reviews = df.groupby('newtime').size()

    mean_reviews_per_day = daily_reviews.mean()

    all_dates = pd.date_range(daily_reviews.index.min(), daily_reviews.index.max())
    daily_reviews = daily_reviews.reindex(all_dates, fill_value=mean_reviews_per_day)

    plt.figure(figsize=(12, 6))
    daily_reviews.plot()
    plt.title('Daily Reviews Trend')
    plt.xlabel('Date')
    plt.ylabel('Number of Reviews')
    plt.savefig("review_trend_clean")

    return  daily_reviews

def seasonal_trend_analysis(df):
    # Convert "newtime" to date format if not already
    daily_reviews = process_reviews(df)

    decomposition = seasonal_decompose(daily_reviews, model='additive')

    plt.figure(figsize=(12, 6))
    decomposition.seasonal.plot()
    plt.title('Seasonality')
    plt.xlabel('Date')
    plt.ylabel('Seasonal Effect')
    plt.savefig("Seasonal Effect in review")

    plt.figure(figsize=(12, 6))
    decomposition.trend.plot()
    plt.title('Trend')
    plt.xlabel('Date')
    plt.ylabel('Trend Effect')
    plt.savefig("trend Effect in review")

    plt.rcParams["figure.figsize"] = (15, 10)
    decomposition.plot().suptitle('review Decompose', fontsize=12)
    plt.savefig("plots_decompose")

    return decomposition


if __name__ == "__main__":
    #1.8.1 reviewer_business_list
    import pandas as pd
    join_review_with_workday = pd.read_csv('join_review_with_workday.csv', low_memory=False)
    daily_reviews = process_reviews(join_review_with_workday)
    seasonal_trend_analysis(join_review_with_workday)

print("12")