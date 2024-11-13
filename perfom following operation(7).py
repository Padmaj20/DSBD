


# Importing required libraries
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

# Load the dataset (ensure the correct file path)
df = pd.read_csv('Assignment 7.csv')

# Display initial statistics
print(df.info())
print(df.describe())

# Handling missing values
df['Age'].fillna(df['Age'].mean(), inplace=True)
df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)

# Handle outliers in numerical columns
numerical_cols = df.select_dtypes(include=np.number).columns
for col in numerical_cols:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    lowerBound = Q1 - 1.5 * IQR
    upperBound = Q3 + 1.5 * IQR
    df[col] = np.where(df[col] < lowerBound, lowerBound, np.where(df[col] > upperBound, upperBound, df[col]))

# Data transformation
scaler = MinMaxScaler()
df[['Age', 'Fare']] = scaler.fit_transform(df[['Age', 'Fare']])

# Encoding categorical variables
df = pd.get_dummies(df, columns=['Sex', 'Embarked'], dtype=int)

# Save the modified DataFrame
df.to_csv('modified_titanic_dataset.csv', index=False)
