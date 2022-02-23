# Crypto Price History Neural Network

## Installation
- Clone repository onto your machine
- Open terminal at project root
- Install dependencies - `pip install -r ./requirements.txt`
    - If there are issues, try `pip3 install -r ./requirements.txt`
- This repo comes with 2015-2022 Bitcoin price history. More can be downloaded at [https://www.
  cryptodatadownload.com/data/bitfinex/](https://www.cryptodatadownload.com/data/bitfinex/).

## Usage
#### csv_ai.py
- To train the neural network, run csv_ai.py.
- Adjust `prediction_days` to suit your needs. This is the amount of previous days the RNN 
  will take into consideration when predicting the next day forward.
- To increase/decrease the cycles over the data set, change the value of `epochs`. `batch_size` 
  can also be changed, default batch size is 32.
- The Keras model will be saved under models/{model_name}

#### plot.py
- Running this file should product a plot of the predicted price against the real price.
- Change the value of `test_column` to a different column in the csv to compare other data.
  - Make sure that the test column exists in both the training set and the testing set.
