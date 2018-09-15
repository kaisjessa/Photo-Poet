import numpy as np
import pandas as pd
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import LSTM
from keras.utils import np_utils

# from data_preprocessing import training_data
# X, y = training_data()
# print(X, y)

with open('training_data.pkl', 'rb') as f:
    X, y = pickle.load(f)

print(X, y)
