#imports
import numpy as np
import pandas as pd
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import LSTM
from keras.utils import np_utils
import pickle

#open text file with poems
text = (open("./text_data/test_poetry2.txt").read()).lower()

#sort list of unique characters in text
chars = sorted(list(set(text)))

#dictionary mapping cchars to ints
char_to_int = {char:n for n,char in enumerate(chars)}
#dictionary mapping ints to chars
int_to_char = {n:char for n,char in enumerate(chars)}

#training and target lists
X,y = [],[]
text_length = len(text)
#length of string given to NN to make prediction
str_length = 100
print("Unique chars:", len(chars))
print("Text length:", text_length)

#loop through text
for i in range(0, text_length - str_length, 1):
    #add a list of length str_length to training data
    X.append([char_to_int[c] for c in text[i : i + str_length]])
    #add the next character in the sequence to target list
    #y[n] will have the character than comes after x[n][str_length-1]
    #we want the NN to predict the next letter based on previous letters
    y.append(char_to_int[text[i + str_length]])

#reshape training data for the NN
X_2 = np.reshape(X, (len(X), str_length, 1))
#normalize the training data so that all values are between 0 and 1
X_2 = X_2 / float(len(chars))
#convert Y to a one-hot array··
y_2 = np_utils.to_categorical(y)


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
model.save("./python_model_training/models/test_model.h5")
print("Training Completed!")
