import pandas as pd

def load_data(path):
    return pd.read_csv(path)

def preprocess_data(df):
    # Drop unnecessary columns (safe)
    df = df.drop(["Id", "PoolQC", "MiscFeature", "Alley", "Fence"], axis=1, errors="ignore")

    # Separate target
    y = df["SalePrice"]
    X = df.drop("SalePrice", axis=1)

    # Fill missing values
    num_cols = X.select_dtypes(include=['int64', 'float64']).columns
    X[num_cols] = X[num_cols].fillna(X[num_cols].median())

    cat_cols = X.select_dtypes(include=['object']).columns
    X[cat_cols] = X[cat_cols].fillna(X[cat_cols].mode().iloc[0])

    # One-hot encoding
    X = pd.get_dummies(X, drop_first=True)

    return X, y