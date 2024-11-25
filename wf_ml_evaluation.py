import pandas as pd
from sklearn.model_selection import train_test_split
from wf_ml_training import train_model_linear, train_model_ridge, train_model_lasso
from wf_ml_prediction import make_predictions
from sklearn.metrics import mean_squared_error, mean_absolute_error, median_absolute_error, accuracy_score


def lasso_inflation_electricity_vs_confidence(df):
    features = ["standard_inflation", "standard_electricity"]
    target = "standard_confidence"
    model_name = "inflation_electricity_vs_confidence_lasso"
    train_and_evaluate_model_lasso(df, features, target, model_name)

def ridge_inflation_electricity_vs_confidence(df):
    features = ["standard_inflation", "standard_electricity"]
    target = "standard_confidence"
    model_name = "inflation_electricity_vs_confidence_ridge"
    train_and_evaluate_model_ridge(df, features, target, model_name)

def inflation_electricity_vs_confidence(df):
    features = ["standard_inflation", "standard_electricity"]
    target = "standard_confidence"
    model_name = "inflation_electricity_vs_confidence"
    train_and_evaluate_model(df, features, target, model_name)

def linear_inflation_vs_confidence(df):
    features = ["standard_inflation"]
    target = "standard_confidence"
    model_name = "gasoline_vs_confidence"
    train_and_evaluate_model(df, features, target, model_name)

def linear_all_vs_confidence_regular(df):
    features = ["inflation", "electricity", "chicken", "gasoline"]
    target = "confidence"
    model_name = "all_vs_confidence_regular"
    train_and_evaluate_model(df, features, target, model_name)

def linear_all_vs_confidence(df):
    features = ["standard_inflation", "standard_electricity", "standard_chicken", "standard_gasoline"]
    target = "standard_confidence"
    model_name = "all_vs_confidence"
    train_and_evaluate_model(df, features, target, model_name)


def evaluate_model(y_test, prediction, model_name):
    summary_file = "evaluation/summary.txt"
    metric = {"MSE": mean_squared_error(y_test, prediction), "MAE": mean_absolute_error(y_test, prediction),
              "MedAE": median_absolute_error(y_test, prediction)}

    with open(summary_file, "a") as q:
        q.write(f"Model: {model_name}\n")
        for m, value in metric.items():
            q.write(f"{m}: {value:.3f}\n")
        q.write("-------------------------------------\n")


def train_and_evaluate_model(df, features, target, model):
    X = df[features]
    y = df[target]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=8)
    train_data = pd.concat([X_train, y_train], axis=1)
    train_data.to_csv(f"data_processed/{model}_train.csv")
    test_data = pd.concat([X_test, y_test], axis=1)
    test_data.to_csv(f"data_processed/{model}_test.csv")
    model_path = f"models/{model}.pkl"
    train_model_linear(X_train, y_train, model_path)
    prediction = make_predictions(X_test, model_path)
    evaluate_model(y_test, prediction, model)



def train_and_evaluate_model_ridge(df, features, target, model):
    X = df[features]
    y = df[target]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=8)
    train_data = pd.concat([X_train, y_train], axis=1)
    train_data.to_csv(f"data_processed/{model}_train.csv")
    test_data = pd.concat([X_test, y_test], axis=1)
    test_data.to_csv(f"data_processed/{model}_test.csv")
    model_path = f"models/{model}.pkl"
    train_model_ridge(X_train, y_train, model_path)
    prediction = make_predictions(X_test, model_path)
    evaluate_model(y_test, prediction, model)
    pass


def train_and_evaluate_model_lasso(df, features, target, model):
    X = df[features]
    y = df[target]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=8)
    train_data = pd.concat([X_train, y_train], axis=1)
    train_data.to_csv(f"data_processed/{model}_train.csv")
    test_data = pd.concat([X_test, y_test], axis=1)
    test_data.to_csv( f"data_processed/{model}_test.csv")
    model_path = f"models/{model}.pkl"
    train_model_lasso(X_train, y_train, model_path)
    prediction = make_predictions(X_test, model_path)
    evaluate_model(y_test, prediction, model)
    pass

if __name__ == '__main__':
    data_path = "data_processed/all.csv"
    df = pd.read_csv(data_path)
    ridge_inflation_electricity_vs_confidence(df)
    lasso_inflation_electricity_vs_confidence(df)
    inflation_electricity_vs_confidence(df)
    linear_inflation_vs_confidence(df)
    linear_all_vs_confidence(df)
    linear_all_vs_confidence_regular(df)
