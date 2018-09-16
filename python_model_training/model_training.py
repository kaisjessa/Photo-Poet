#imports
import numpy as np
import pandas as pd
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import LSTM
from keras.utils import np_utils
import pickle
from data_preprocessing import X_2, y_2

#Keras NN
model = Sequential()
#add long short term memory cell
#output is 400 units (length), input_shape is (number_of_inputs, input_length), return full sequence
model.add(LSTM(700, input_shape=(X_2.shape[1], X_2.shape[2]), return_sequences=True)) #layer 1
#account for overfitting
model.add(Dropout(0.2))

#add another LSTM layer
model.add(LSTM(700)) #layer 2
#account for overfitting
model.add(Dropout(0.2))

#Fully connected (dense) output layer
model.add(Dense(y_2.shape[1], activation='softmax')) #layer 3
#minimize loss
model.compile(loss='categorical_crossentropy', optimizer='adam')
#train the model
model.fit(X_2, y_2, epochs=100, batch_size=50)
#save the model
#----model.save("./python_model_training/models/test_model.h5")
print("Training Completed!")
