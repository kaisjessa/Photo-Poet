#imports
import numpy as np
from keras.utils import np_utils
import pickle

#open text file with poems
text = (open("text_data/test_poetry4.txt").read()).lower()

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

with open('models/objects.pkl', 'wb') as f:
    pickle.dump([X, y, char_to_int, int_to_char, chars], f)
