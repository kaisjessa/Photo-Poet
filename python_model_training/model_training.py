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
    X, y, _, _, _ = pickle.load(f)

#Keras NN
model = Sequential()
#add long short term memory cell
#output is 400 units (length), input_shape is (number_of_inputs, input_length), return full sequence
#LAYER 1 (input layer)
model.add(LSTM(400, input_shape=(X.shape[1], X.shape[2]), return_sequences=True))
#account for overfitting
model.add(Dropout(0.2))
#add another LSTM layer
#LAYER 2 (hidden layer)
model.add(LSTM(400))
#account for overfitting
model.add(Dropout(0.2))
#Fully connected (dense) output layer
#LAYER 3 (output layer)
model.add(Dense(y.shape[1], activation='softmax'))
#minimize loss
model.compile(loss='categorical_crossentropy', optimizer='adam')
#train the model
model.fit(X, y, epochs=1, batch_size=100)
#save the model
model.save("./python_model_training/models/test_model.h5")
print("Works!")
