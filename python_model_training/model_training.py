#Python script for training the machine learning model
#imports
import numpy as np
from keras.callbacks import ModelCheckpoint
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import LSTM
from keras.utils import np_utils
from char_data_preprocessing import *
#Keras NN
model = Sequential()
#add long short term memory cell
#output_shape is (_, 700), input_shape is (number_of_inputs, input_length), return full sequence
model.add(LSTM(700, input_shape=(X_2.shape[1], X_2.shape[2]), return_sequences=True)) #layer 1
#account for overfitting
model.add(Dropout(0.2))

#add another LSTM layer
model.add(LSTM(700, return_sequences=True)) #layer 2
#account for overfitting
model.add(Dropout(0.2))

#add another LSTM layer
model.add(LSTM(700)) #layer 3
#account for overfitting
model.add(Dropout(0.2))

#Fully connected (dense) output layer
model.add(Dense(y_2.shape[1], activation='softmax')) #layer 4
#minimize loss
model.compile(loss='categorical_crossentropy', optimizer='adam')
print("Model compiled")

filepath = "models/current_best_model.h5"
checkpoint = ModelCheckpoint(filepath, monitor='loss', verbose=1, save_best_only=True, mode='min')
callbacks_list = [checkpoint]

#train the model
model.fit(X_2, y_2, epochs=100, batch_size=50, callbacks=callbacks_list)
#save the model
model.save("final_model.h5")
print("Training Completed!")
