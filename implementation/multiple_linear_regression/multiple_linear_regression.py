# -*- coding: utf-8 -*-
"""multiple_linear_regression.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1h-yfTJy1s7NR27XVQJ6lj9sD_8zojgkr

# Prediction using a multiple linear regression model
"""

import numpy as np
import pandas as pd

"""# Import and split the dataset"""

dataset = pd.read_csv('train.csv')
dataset.head()
X = dataset.iloc[:, [0, 2, 6, 7]].values
y = dataset.iloc[:, 1].values

"""# Have a summary of the dataset"""

dataset.info()

"""# Look for null values in the dataset

"""

dataset.isnull().sum() # Here we can see that we have null values on many Age information from Passengers, there fore to base the prediction in the age would output a biased result

"""# Splitting the dataset into the training and test set"""

testDataset = pd.read_csv('test.csv')
testDataset.isnull().sum()
X_test = testDataset.iloc[:, [0, 1, 5, 6]].values
y_test = testDataset.iloc[:, 1].values
print(X_test)

"""# Training the multiple linear regression model on the training set"""

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X, y)

"""#Predictin the test set results"""

rawPredictions = regressor.predict(X_test)
predictions = []
for x in rawPredictions:
  if x > 0.45: predictions.append(1)
  else: predictions.append(0)

deaths = predictions.count(0)
output = pd.DataFrame({'PassengerId': X_test[:, 0], 'Survived': predictions})
output.to_csv('submission5.csv', index=False)
print('Submission saved with deaths/total', deaths, '/', len(X_test))