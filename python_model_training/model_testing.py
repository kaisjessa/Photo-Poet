#imports
import numpy as np
import pandas as pd
import random
import keras.models
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import LSTM
from keras.utils import np_utils
from data_preprocessing import *

#load model
model = keras.models.load_model("models/medium_model_002.h5")

#take random line of integer training data as starting input
int_train = X[random.randint(0, len(X))]

#convert training data back to array of chars
chars_array = [int_to_char[n] for n in int_train]
starting_text = '\n' + ''.join(chars_array) + '\n'


#number of characters to generate
for i in range(400):
    #reshape data to feed to NN
    x = np.reshape(int_train, (1, len(int_train), 1))
    #normalize for NN
    x = x / float(len(chars))

    #the prediction is the index of the next character index
    #argmax takes the highest number in the onehot array
    int_prediction = np.argmax(model.predict(x, verbose=0))
    #print(model.predict(x, verbose=0))

    #append prediction to string array for output
    chars_array.append(int_to_char[int_prediction])

    #append index to index array
    int_train.append(int_prediction)
    #drop first element for next iteration
    int_train = int_train[1:len(int_train)]

predicted_text = ""
for c in chars_array[100:]:
    predicted_text += c
print("Starting text: ", starting_text)
print("Predicted text: ", predicted_text)