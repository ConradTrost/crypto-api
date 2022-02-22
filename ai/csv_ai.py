"""
Recurrent Neural Network
"""

import numpy as np
import pandas as pd
import os
from tensorflow import keras
from sklearn.preprocessing import MinMaxScaler

dataset_train = pd.read_csv('../data/btc_2015-2020.csv')
training_set = dataset_train.iloc[:, 1:2].values
prediction_days = 30

sc = MinMaxScaler(feature_range=(0, 1))
training_set_scaled = sc.fit_transform(training_set)
X_train = []
y_train = []
for i in range(prediction_days, len(dataset_train)):
    X_train.append(training_set_scaled[i - prediction_days:i, 0])
    y_train.append(training_set_scaled[i, 0])
X_train, y_train = np.array(X_train), np.array(y_train)
X_train = np.reshape(X_train, (X_train.shape[0], X_train.shape[1], 1))

if os.path.isdir('../models/btc01'):
    model = keras.models.load_model('../models/btc01')
    print('\nModel loaded from ../models/btc01...\n')
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
    print(f'\nNew model {model.name} created...\n')

model.compile(optimizer='adam', loss='mean_squared_error')


def _int_validator(input_type):
    while True:
        try:
            return int(input(f'Enter {input_type}: '))
        except ValueError:
            print('Please enter a valid integer')
            continue


epochs = _int_validator('Epochs')

model.fit(X_train, y_train, epochs=epochs, batch_size=len(dataset_train))
model.save('../models/btc01')

try:
    model.save('../models/btc01')
except:
    print('Model could not be saved')
else:
    print('Model saved in ../models/btc01')
