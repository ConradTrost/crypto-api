"""
Recurrent Neural Network
"""

import numpy as np
import pandas as pd
import os
from tensorflow import keras
from sklearn.preprocessing import MinMaxScaler

# Importing the training set
dataset_train = pd.read_csv('../data/btc_2015-2020.csv')

training_set = dataset_train.iloc[:, 1:2].values

prediction_days = 30

# Feature Scaling
sc = MinMaxScaler(feature_range=(0, 1))
training_set_scaled = sc.fit_transform(training_set)

# Creating a data structure with 10 time-steps and 1 output
X_train = []
y_train = []
for i in range(prediction_days, len(dataset_train)):
    X_train.append(training_set_scaled[i - prediction_days:i, 0])
    y_train.append(training_set_scaled[i, 0])
X_train, y_train = np.array(X_train), np.array(y_train)

# Reshaping
X_train = np.reshape(X_train, (X_train.shape[0], X_train.shape[1], 1))

# Initialize RNN
if os.path.isdir('../models/btc01'):
    model = keras.models.load_model('../models/btc01')
else:
    model = keras.models.Sequential([
        keras.layers.LSTM(units=50, return_sequences=True, input_shape=(X_train.shape[1], 1), name="layer1"),
        keras.layers.Dropout(0.2),
        keras.layers.LSTM(units=50, return_sequences=True, name="layer2"),
        keras.layers.Dropout(0.2),
        keras.layers.LSTM(units=50, return_sequences=True, name="layer3"),
        keras.layers.Dropout(0.2),
        keras.layers.LSTM(units=50, name="layer4"),
        keras.layers.Dropout(0.2),
        keras.layers.Dense(units=1),
    ], name="sequential1")

# Compiling the RNN
model.compile(optimizer='adam', loss='mean_squared_error')

# Fitting the RNN to the Training set
model.fit(X_train, y_train, epochs=10, batch_size=len(dataset_train))

model.save('../models/btc01')
