import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression

# Load the dataset from a URL and select only the specified features
url = "http://s3.amazonaws.com/assets.datacamp.com/course/Kaggle/train.csv"
df = pd.read_csv(filepath_or_buffer=url)
selected_features = ['Age', 'Sex', 'Embarked', 'Survived']  # We're interested in these four features
df = df[selected_features]


# Data Preprocessing
categorical_columns = []                # To store categorical columns
for col in df.columns:
    data_type = df[col].dtype
    if data_type == 'O':  # Check if the column has object data type (categorical)
        categorical_columns.append(col)
    else:
        df[col].fillna(value=0, inplace=True)  # Fill missing values in non-categorical columns with 0


# Perform one-hot encoding on categorical columns
df_encoded = pd.get_dummies(data=df, columns=categorical_columns, dummy_na=True)


# Define the dependent variable and split data into features (x) and target (y)
dependent_variable = 'Survived'
x = df_encoded[df_encoded.columns.difference([dependent_variable])]
y = df_encoded[dependent_variable]


# Create and train a Logistic Regression classifier
lr = LogisticRegression()
lr.fit(X=x, y=y)

import joblib
joblib.dump(lr, 'MLmodels/lr_model.pkl')
joblib.dump(x.columns, 'MLmodels/lr_model_columns.pkl')