import pickle
import numpy as np
import pandas as pd

def make_predictions(x_test, model_file_path):
    with open(model_file_path, 'rb') as model_file:
        model = pickle.load(model_file)
    prediction = model.predict(x_test)
    return prediction

def runInput():
    print("we will be using the most effective model based on summary.txt (all_vs_confidence) without standardization")
    chicken = input("input price of chicken: \n")
    electricity = input("input price of electricity per KwH: \n")
    inflation = input("input rate of inflation: \n")
    gasoline = input("input price of gas per gallon: \n")
    print("features being used for prediction of consumer confidence:")
    features = [inflation, electricity, chicken, gasoline]
    features = np.array(features).reshape(1, -1)
    names = ['inflation', 'electricity', 'chicken', 'gasoline']
    df = pd.DataFrame(features, columns=names)
    df.to_csv('data_processed/consumer_confidence_input.csv', index=False)
    df = pd.read_csv('data_processed/consumer_confidence_input.csv')
    print(df)
    prediction =  make_predictions(df, "models/all_vs_confidence_regular.pkl")
    print("\nprediction output: ", prediction[0])
    pass


if __name__ == '__main__':
    runInput()