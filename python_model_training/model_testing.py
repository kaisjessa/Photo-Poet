#imports
import numpy as np
import pandas as pd
import pickle
import keras.models
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import LSTM
from keras.utils import np_utils

with open('./python_model_training/models/training_data.pkl', 'rb') as f:
    X, y, str_length, char_to_int, int_to_char = pickle.load(f)

#load model
keras.models.load_model("./python_model_training/models/test_model.h5")

#choose random row from training data
str = X[99]
print(str)
for i in range(str_length):
    x = np.reshape(str, (1, len(str), 1))
    print(x)
