import pandas as pd
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt

from sklearn.preprocessing import MinMaxScaler

sc = MinMaxScaler(feature_range=(0, 1))

dataset_train = pd.read_csv('../data/btc_2015-2020.csv')

training_set = dataset_train.iloc[:, 1:2].values
training_set_scaled = sc.fit_transform(training_set)

prediction_days = 30

# Getting the real stock price of 2017
dataset_test = pd.read_csv('../data/btc_2020-now.csv')

real_stock_price = dataset_test.iloc[:, 1:2].values

model = keras.models.load_model('../models/btc01')

# Getting the predicted stock price of 2017
dataset_total = pd.concat((dataset_train['close'], dataset_test['close']), axis=0)
inputs = dataset_total[len(dataset_total) - len(dataset_test) - prediction_days:].values
inputs = inputs.reshape(-1, 1)
inputs = sc.transform(inputs)
X_test = []
for i in range(prediction_days, len(dataset_test) + prediction_days):
    X_test.append(inputs[i - prediction_days:i, 0])
X_test = np.array(X_test)
X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1))
predicted_stock_price = model.predict(X_test)
predicted_stock_price = sc.inverse_transform(predicted_stock_price)

# Visualising the results
plt.plot(real_stock_price, color='red', label='Real Bitcoin Price')
plt.plot(predicted_stock_price, color='blue', label='Predicted Bitcoin Price')
plt.title('Bitcoin Prediction')
plt.xlabel('Time')
plt.ylabel('Bitcoin Price')
plt.grid()
plt.legend()
plt.show()
