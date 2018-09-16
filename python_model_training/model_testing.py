#imports
import numpy as np
import pandas as pd
import random
import keras.models
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import LSTM
from keras.utils import np_utils
import pickle, sys
#from data_preprocessing import *

with open('models/objects.pkl', 'rb') as f:  # Python 3: open(..., 'rb')
    X, y, char_to_int, int_to_char, chars = pickle.load(f)

#load model
model = keras.models.load_model("models/medium_model_012.h5")
# model = keras.models.load_model("models/current_best_model.h5")

model_json = model.to_json()
with open("models/model.json", "w") as f:
    f.write(model_json)

sample_word = "falling"# if len(sys.argv) < 2 else sys.argv[1]
def check_model(keyword):
    #take random line of integer training data as starting input
    if len(keyword) > 0:
        int_train = X[random.randint(0, len(X))][:-len(keyword)]
        for c in keyword:
            int_train.append(char_to_int[c])
    else:
        int_train = X[random.randint(0, len(X))]
    #convert training data back to array of chars
    chars_array = [int_to_char[n] for n in int_train]
    #print(chars_array)
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
    for c in chars_array[100-len(keyword):]:
        predicted_text += c
    #return(predicted_text[predicted_text.find('\n'):predicted_text.rfind('\n')])
    return(predicted_text)
print(check_model(sample_word))
