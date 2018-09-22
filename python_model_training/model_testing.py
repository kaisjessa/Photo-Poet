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
    X, y, word_to_int, int_to_word, words = pickle.load(f)

text = (open("text_data/test_poetry4.txt").read())#.lower()
words = sorted(list(set(text.split(" "))))

#load model
model = keras.models.load_model("models/medium_model_015.h5")
# model = keras.models.load_model("models/current_best_model.h5")

model_json = model.to_json()
with open("models/model.json", "w") as f:
    f.write(model_json)

#sample_word = "" if len(sys.argv) < 2 else sys.argv[1]
#take an array of inputs
poem_array = ""
sample_word_array = [""] if len(sys.argv) < 2 else sys.argv[1]
def check_model(keyword_array):
    for keyword in keyword_array:
        if len(keyword_array) > 0:
            int_train = X[random.randint(0, len(X))][:-len(keyword)]
            for c in keyword:
                int_train.append(word_to_int[c])
        else:
            int_train = X[random.randint(0, len(X))]
        #convert training data back to array of words
        words_array = [int_to_word[n] for n in int_train]
        #print(words_array)
        #starting_text = '\n' + ''.join(words_array) + '\n'

        #number of characters to generate
        for i in range(20):
            #reshape data to feed to NN
            x = np.reshape(int_train, (1, len(int_train), 1))
            #normalize for NN
            x = x / float(len(words))

            #the prediction is the index of the next character index
            #argmax takes the highest number in the onehot array
            int_prediction = np.argmax(model.predict(x, verbose=0))
            #print(model.predict(x, verbose=0))

            #append prediction to string array for output
            words_array.append(int_to_word[int_prediction])
            poem_array.append(int_to_word[int_prediction])

            #append index to index array
            int_train.append(int_prediction)
            #drop first element for next iteration
            int_train = int_train[1:len(int_train)]

        predicted_text = "".join(poem_array)
    #return(predicted_text[predicted_text.find('\n'):predicted_text.rfind('\n')])
    return(predicted_text[:predicted_text.rfind('\n')])
print(check_model(sample_word_array))
