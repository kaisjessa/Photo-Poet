#imports
import numpy as np
import pandas as pd
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import LSTM
from keras.utils import np_utils
import pickle

#open training data pickle
with open('./python_model_training/models/training_data.pkl', 'rb') as f:
    X, y = pickle.load(f)
