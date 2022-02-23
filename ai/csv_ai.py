"""
Recurrent Neural Network
"""
import numpy as np
import pandas as pd
import os
from tensorflow import keras
from sklearn.preprocessing import MinMaxScaler

epochs = 100
model_name = 'btc01'
trainCSV = '../data/btc_2015-2020.csv'
prediction_days = 30

dataset_train = pd.read_csv(trainCSV)
training_set = dataset_train.iloc[:, 1:2].values

sc = MinMaxScaler(feature_range=(0, 1))
training_set_scaled = sc.fit_transform(training_set)
X_train = []
y_train = []
for i in range(prediction_days, len(dataset_train)):
    X_train.append(training_set_scaled[i - prediction_days:i, 0])
    y_train.append(training_set_scaled[i, 0])
X_train, y_train = np.array(X_train), np.array(y_train)
X_train = np.reshape(X_train, (X_train.shape[0], X_train.shape[1], 1))

if os.path.isdir(f'../models/{model_name}'):
    model = keras.models.load_model(f'../models/{model_name}')
    print(f'\nModel loaded from ../models/{model_name}\n')
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
    ], name=model_name)
    print(f'\nNew model {model.name} created...\n')

model.compile(optimizer='adam', loss='mean_squared_error')
# Update batch_size depending on your hardware capabilities. Default is 32
model.fit(X_train, y_train, epochs=epochs, batch_size=len(dataset_train))

try:
    model.save(f'../models/{model_name}')
except:
    print('\nModel could not be saved\n')
else:
    print(f'\nModel saved in ../models/{model_name}\n')

print(model.summary())
