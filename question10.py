
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose
from question9 import process_reviews

def arima_model02(series):
    from pyspark.sql import SparkSession
    from statsmodels.tsa.arima.model import ARIMA
    from sklearn.metrics import mean_squared_error
    from math import sqrt
    import pandas as pd

    # Initialize Spark session
    spark = SparkSession.builder \
        .appName("ARIMA Model Training") \
        .getOrCreate()

    train_size = int(len(series) * 0.7)
    train, test = series[0:train_size], series[train_size:len(series)]
    history_initial = [x for x in train]
    results = []

    # Define parameter grid to search
    param_grid = [(p, d, q) for p in [0,1,2] for d in [0,1,2] for q in [0,1,2]]
    param_rdd = spark.sparkContext.parallelize(param_grid)

    def evaluate_params(params):
        i1, i3, i2 = params
        history = history_initial.copy()
        predictions = []

        try:
            for t in range(len(test)):
                model = ARIMA(history, order=(i1, i3, i2))
                model_fit = model.fit()
                output = model_fit.forecast(steps=1)
                yhat = output[0]
                predictions.append(yhat)
                obs = test.iloc[t] if hasattr(test, 'iloc') else test[t]
                history.append(obs)

            if all(p is not None for p in predictions) and len(predictions) == len(test):
                rmse = sqrt(mean_squared_error(test, predictions))
                return {
                    'p': i1,
                    'd': i3,
                    'q': i2,
                    'rmse': rmse
                }
        except Exception as e:
            print(f"Error with order ({i1},{i3},{i2}): {e}")

        return None

    # Apply the evaluation function to each parameter set
    results = param_rdd.map(evaluate_params).filter(lambda x: x is not None).collect()

    results_df = pd.DataFrame(results)
    results_df.to_csv('arima_results.csv', index=False)

    if not results_df.empty:
        best_params = results_df.loc[results_df['rmse'].idxmin()]
        print(
            f"\nBest parameters: p={best_params['p']}, d={best_params['d']}, q={best_params['q']}, RMSE={best_params['rmse']:.3f}")

    return results_df, train, test

def arima_predict(test,p,d,q):
    from statsmodels.tsa.arima.model import ARIMA
    from sklearn.metrics import mean_squared_error
    from math import sqrt
    import matplotlib.pyplot as plt
    import numpy as np

    confidence_interval = []
    history_initial = [x for x in train]
    predictions = []

    # walk-forward validation
    for t in range(len(test)):
        model = ARIMA(history_initial, order=(p, d, q))
        model_fit = model.fit()
        output = model_fit.get_forecast()
        yhat = output.predicted_mean
        predictions.append(yhat)
        obs = test[t]
        history = history_initial.copy()
        history.append(obs)
        print('predicted=%f, expected=%f' % (yhat, obs))
        ci = output.conf_int(0.05)
        confidence_interval.append(ci[0])
        print('95%% Interval: %.3f to %.3f' % (ci[0, 0], ci[0, 1]))

    # evaluate forecasts
    rmse = sqrt(mean_squared_error(test, predictions))
    print('Test RMSE: %.3f' % rmse)

    # plot forecasts against actual outcomes and also the confidence int at 95%
    plt.plot(test)
    plt.plot(predictions, color='red')
    plt.fill_between(list(range(len(test))),
                        np.array(confidence_interval)[:, 0], np.array(confidence_interval)[:, 1],
                        alpha=0.1, color='b')
    plt.show()


def arima_predict(train, test, p, d, q):
    from statsmodels.tsa.arima.model import ARIMA
    from sklearn.metrics import mean_squared_error
    from math import sqrt
    import matplotlib.pyplot as plt
    import numpy as np

    confidence_interval = []
    history = list(train)
    predictions = []
    results = []

    # walk-forward validation
    for t in range(len(test)):
        model = ARIMA(history, order=(p, d, q))
        model_fit = model.fit()
        output = model_fit.forecast(steps=1)
        yhat = output[0]
        predictions.append(yhat)

        obs = test[t]
        history.append(obs)  # Update history with observed value
        print(f'predicted={yhat:.3f}, expected={obs:.3f}')

        ci = model_fit.get_forecast(steps=1).conf_int(alpha=0.05)
        confidence_interval.append((ci[0, 0], ci[0, 1]))
        print(f'95% Interval: {ci[0, 0]:.3f} to {ci[0, 1]:.3f}')

        # Save result
        results.append((yhat, obs, ci[0, 0], ci[0, 1]))
    # evaluate forecasts
    rmse = sqrt(mean_squared_error(test, predictions))
    print(f'Test RMSE: {rmse:.3f}')

    # Save to CSV
    results_df = pd.DataFrame(results, columns=['Predicted', 'Expected', 'CI Lower', 'CI Upper'])
    # results_df.to_csv('arima_predictions.csv', index=False)

    # plot forecasts against actual outcomes and also the confidence intervals at 95%
    # plt.plot(test.reset_index(drop=True), label='Actual')
    # plt.plot(predictions, color='red', label='Predictions')
    plt.plot(test.reset_index(drop=True), label='Actual', color='orange', linewidth=2)
    plt.plot(predictions, color='red', linestyle='--', label='Predictions', linewidth=2)
    plt.fill_between(
        np.arange(len(test)),
        np.array(confidence_interval)[:, 0],
        np.array(confidence_interval)[:, 1],
        color='blue', alpha=0.3, label='95% Confidence Interval'
    )
    plt.legend()
    plt.title("Daily Reviews Trend")
    plt.xlabel("Date")
    plt.ylabel("Number of Reviews")
    plt.savefig("arima_prediction_plot.png")
    # plt.show()

    return results_df

if __name__ == "__main__":
    #1.10 ARIMA model
    import pandas as pd
    join_review_with_workday = pd.read_csv('join_review_with_workday.csv', low_memory=False)
    daily_reviews = process_reviews(join_review_with_workday)

    train_size = int(len(daily_reviews) * 0.7)
    train, test = daily_reviews[0:train_size], daily_reviews[train_size:len(daily_reviews)]

    #training model
    results_df, train, test = arima_model02(daily_reviews)

    #get predict values
    # predict_df =arima_predict(train, test, 1, 0, 1)  #test[::2]


print("13")

