#imports
import numpy as np
import pandas as pd
import pickle
import random
import keras.models
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import LSTM
from keras.utils import np_utils

with open('./python_model_training/models/training_data.pkl', 'rb') as f:
    X_2, y_2, str_length, _, int_to_char, chars, X, y = pickle.load(f)

#load model
model = keras.models.load_model("./python_model_training/models/test_model.h5")

#take random line of integer training data
int_train = X[10]


#convert training data back to array of chars
chars_array = [int_to_char[n] for n in int_train]
print(chars_array)


#number of characters to generate
# num_chars = 1000
for i in range(5):
    #reshape data to feed to NN
    x = np.reshape(int_train, (1, len(int_train), 1))
    x = x / float(len(chars))
    #print(x)

    #the prediction is the index of the next character index
    #argmax takes the highest number in the onehot array
    int_prediction = np.argmax(model.predict(x, verbose=0))
    print(model.predict(x, verbose=0))

    #append prediction to string array for output
    chars_array.append(int_to_char[int_prediction])
    #print(model.predict(x, verbose=0))
    #print(np.argmax(model.predict(x, verbose=0)))

    #append index to index array
    int_train.append(int_prediction)
    #
    int_train = int_train[1:len(int_train)]
text = ""
print(chars_array)