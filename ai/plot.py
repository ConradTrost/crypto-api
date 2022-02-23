import pandas as pd
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from csv_ai import dataset_train, prediction_days, model_name

dataset_test = pd.read_csv('../data/btc_2020-now.csv')
model = keras.models.load_model(f'../models/{model_name}')
test_column = 'open'

sc = MinMaxScaler(feature_range=(0, 1))
training_set = dataset_train.iloc[:, 1:2].values
training_set_scaled = sc.fit_transform(training_set)
real_price = dataset_test.iloc[:, 1:2].values

dataset_total = pd.concat((dataset_train[test_column], dataset_test[test_column]), axis=0)
inputs = dataset_total[len(dataset_total) - len(dataset_test) - prediction_days:].values
inputs = inputs.reshape(-1, 1)
inputs = sc.transform(inputs)
X_test = []
for i in range(prediction_days, len(dataset_test) + prediction_days):
    X_test.append(inputs[i - prediction_days:i, 0])
X_test = np.array(X_test)
X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1))
predicted_price = model.predict(X_test)
predicted_price = sc.inverse_transform(predicted_price)

# Plotting graphs
plt.plot(real_price, color='red', label='Real Price')
plt.plot(predicted_price, color='blue', label='Predicted Price')
plt.title('RNN Price prediction')
plt.xlabel('Time')
plt.ylabel('Price')
plt.grid()
plt.legend()
plt.show()
