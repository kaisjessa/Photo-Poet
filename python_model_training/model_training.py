#import
import numpy as np
import pandas as pd
# from keras.models import Sequential
# from keras.layers import Dense
# from keras.layers import Dropout
# from keras.layers import LSTM
# from keras.utils import np_utils

text = (open("./text_data/test_data.txt").read()).lower()

chars = sorted(list(set(text)))
print(chars)
