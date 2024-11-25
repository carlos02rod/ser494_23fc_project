import pickle
from sklearn.linear_model import LinearRegression, Ridge, Lasso

def train_model_linear(X_train, y_train, model_file_path):
    model = LinearRegression()
    model.fit(X_train, y_train)
    with open(model_file_path, 'wb') as model_file:
        pickle.dump(model, model_file)
    print("model trained... linear")


def train_model_ridge(X_train, y_train, model_file_path):
    model = Ridge()
    model.fit(X_train, y_train)
    with open(model_file_path, 'wb') as model_file:
        pickle.dump(model, model_file)
    print("model trained... ridge")


def train_model_lasso(X_train, y_train, model_file_path):
    model = Lasso()
    model.fit(X_train, y_train)
    with open(model_file_path, 'wb') as model_file:
        pickle.dump(model, model_file)
    print("model trained... lasso")