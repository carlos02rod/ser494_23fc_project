import pandas as pd
import matplotlib.pyplot as plt

__author__ = "Carlos Rodriguez"
__date__ = "10/15/24"
__assignment = "SER494: Project Visualization"

def summary_statistics(dataframe, output):
    quant = ["chicken", "electricity", "gasoline", "inflation"]
    qualit = ["gasoline","confidence"]
    quant_sum = {}
    qualit_sum = {}
    for col in quant:
        quant_sum[col] = {
            "min": dataframe[col].min(),
            "max": dataframe[col].max(),
            "median": dataframe[col].median()
        }

    for col in qualit:
        category = dataframe[col].value_counts()
        most_frequent = category[category == category.max()].index.tolist()
        least_frequent = category[category == 1].index.tolist()
        qualit_sum[col] = {
            "num_categories": category.size,
            "most_frequent": most_frequent,
            "least_frequent": least_frequent
        }

    with open(output, 'w') as f:
        f.write("Quantitative Summary Statistics\n")
        f.write("-------------------------------\n")
        f.write("Category   |    Min            Max            Median\n")
        f.write("------------------------------------------------------------\n")
        for category, num in quant_sum.items():
            f.write(f"{category:<15}")
            for stat_value in num.values():
                f.write(f"{stat_value:<15}")
            f.write("\n")
        f.write("------------------------------------------------------------\n")
        f.write("\n")
        f.write("Qualitative Summary Statistics\n")
        f.write("-------------------------------\n")
        f.write("Category   |   # of Categories        Most Freq       Least Freq\n")
        f.write("------------------------------------------------------------\n")
        for category, stats in qualit_sum.items():
            f.write(f"{category:<15}")
            f.write(str(stats["num_categories"]))
            f.write("                    ")
            f.write(str(stats["most_frequent"]))
            f.write("           ")
            f.write(str(stats["least_frequent"]))
            f.write("\n")
        f.write("------------------------------------------------------------\n")
        f.close()
        return quant_sum
    pass


def compute_correlation(output, corr):
    df = pd.DataFrame(corr)
    correlation_matrix = df.corr()
    with open(output, "w") as f:
        f.write(correlation_matrix.to_string())
    pass


def scatterplot_electricity_chicken(processed_data, dates):
    chicken_prices = processed_data["standard_chicken"]
    electricity_prices = processed_data["standard_electricity"]
    plt.figure(figsize=(10, 3))
    plt.scatter(dates, chicken_prices, color="blue", label="Chicken Prices", marker="o")
    plt.scatter(dates, electricity_prices, color="orange", label="Electricity Prices", marker="x")
    plt.xlabel("Date (Year-Month)")
    plt.ylabel("Prices (Dollars per lbs/Kwh)")
    plt.title("Chicken Prices vs Electricity Prices Over Time")
    plt.xticks(ticks=range(0, len(dates), 5), labels=dates[::5], rotation=40)
    plt.legend()
    plt.tight_layout()
    plt.savefig("visuals/chicken_electricity_scatterplot.png")
    plt.close()
    pass


def scatterplot_chicken_gasoline(processed_data, dates):
    chicken_prices = processed_data["standard_chicken"]
    gasoline_prices = processed_data["standard_gasoline"]
    plt.figure(figsize=(10, 3))
    plt.scatter(dates, chicken_prices, color="blue", label="Chicken Prices", marker="o")
    plt.scatter(dates, gasoline_prices, color="orange", label="Gasoline Prices", marker="x")
    plt.xlabel("Date (Year-Month)")
    plt.ylabel("Prices")
    plt.title("Chicken Prices vs Gasoline Prices Over Time")
    plt.xticks(ticks=range(0, len(dates), 5), labels=dates[::5], rotation=40)
    plt.legend()
    plt.tight_layout()
    plt.savefig("visuals/chicken_gasoline_scatterplot.png")
    plt.close()
    pass


def scatterplot_chicken_inflation(processed_data, dates):
    chicken_prices = processed_data["standard_chicken"]
    inflation_prices = processed_data["standard_inflation"]
    plt.figure(figsize=(10, 3))
    plt.scatter(dates, chicken_prices, color="blue", label="Chicken Prices", marker="o")
    plt.scatter(dates, inflation_prices, color="orange", label="Inflation Prices", marker="x")
    plt.xlabel("Date (Year-Month)")
    plt.ylabel("Prices")
    plt.title("Inflation vs Gasoline Prices Over Time")
    plt.xticks(ticks=range(0, len(dates), 5), labels=dates[::5], rotation=40)
    plt.legend()
    plt.tight_layout()
    plt.savefig("visuals/chicken_inflation_scatterplot.png")
    plt.close()
    pass


def scatterplot_electricity_gasoline(processed_data, dates):
    electricity_prices = processed_data["standard_electricity"]
    gasoline_prices = processed_data["standard_gasoline"]
    plt.figure(figsize=(10, 3))
    plt.scatter(dates, electricity_prices, color="blue", label="Electricity Prices", marker="o")
    plt.scatter(dates, gasoline_prices, color="orange", label="Gasoline Prices", marker="x")
    plt.xlabel("Date (Year-Month)")
    plt.ylabel("Prices")
    plt.title("Electricity vs Gasoline Prices Over Time")
    plt.xticks(ticks=range(0, len(dates), 5), labels=dates[::5], rotation=40)
    plt.legend()
    plt.tight_layout()
    plt.savefig("visuals/electricity_gasoline_scatterplot.png")
    plt.close()
    pass


def scatterplot_electricity_inflation(processed_data, dates):
    electricity_prices = processed_data["standard_electricity"]
    inflation_prices = processed_data["standard_inflation"]
    plt.figure(figsize=(10, 3))
    plt.scatter(dates, electricity_prices, color="blue", label="Electricity Prices", marker="o")
    plt.scatter(dates, inflation_prices, color="orange", label="Inflation Prices", marker="x")
    plt.xlabel("Date (Year-Month)")
    plt.ylabel("Prices")
    plt.title("Electricity vs Inflation Prices Over Time")
    plt.xticks(ticks=range(0, len(dates), 5), labels=dates[::5], rotation=40)
    plt.legend()
    plt.tight_layout()
    plt.savefig("visuals/electricity_inflation_scatterplot.png")
    plt.close()
    pass


def scatterplot_gasoline_inflation(processed_data, dates):
    gasoline_prices = processed_data["standard_gasoline"]
    inflation_prices = processed_data["standard_inflation"]
    plt.figure(figsize=(10, 3))
    plt.scatter(dates, gasoline_prices, color="blue", label="Gasoline Prices", marker="o")
    plt.scatter(dates, inflation_prices, color="orange", label="Inflation Prices", marker="x")
    plt.xlabel("Date (Year-Month)")
    plt.ylabel("Prices")
    plt.title("Gasoline vs Inflation Prices Over Time")
    plt.xticks(ticks=range(0, len(dates), 5), labels=dates[::5], rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.savefig("visuals/inflation_gasoline_scatterplot.png")
    plt.close()
    pass


def histogram_confidence(df):
    confidence = df["confidence"]
    plt.figure(figsize=(10, 6))
    plt.hist(confidence,bins=10, color="orange", label="Confidence Levels")
    plt.xlabel("Levels")
    plt.ylabel("Instance")
    plt.title("Confidence Levels with Histogram")
    plt.legend()
    plt.tight_layout()
    plt.savefig("visuals/confidence_histogram.png")
    plt.close()
    pass


def histogram_gasoline(df):
    gasoline = df["gasoline"]
    plt.figure(figsize=(10, 6))
    plt.hist(gasoline,bins=10, color="orange", label="Gasoline Prices")
    plt.xlabel("Prices")
    plt.ylabel("Instance")
    plt.title("Gasoline Prices with Histogram")
    plt.legend()
    plt.tight_layout()
    plt.savefig("visuals/gasoline_histogram.png")
    plt.close()
    pass

def run():
    df = pd.read_csv("data_processed/all.csv")
    output_summary = "data_processed/summary.txt"
    output_correlation = "data_processed/correlations.txt"
    correlation = summary_statistics(df, output_summary)
    compute_correlation(output_correlation, correlation)
    dates = df["dates"]
    dates_new = []
    for d in dates:
        dates_new.append(pd.to_datetime(d).strftime("%y-%m"))
    scatterplot_electricity_chicken(df, dates_new)
    scatterplot_chicken_gasoline(df, dates_new)
    scatterplot_chicken_inflation(df, dates_new)
    scatterplot_electricity_gasoline(df, dates_new)
    scatterplot_electricity_inflation(df, dates_new)
    scatterplot_gasoline_inflation(df, dates_new)
    histogram_confidence(df)
    histogram_gasoline(df)


if __name__ == '__main__':
    run()