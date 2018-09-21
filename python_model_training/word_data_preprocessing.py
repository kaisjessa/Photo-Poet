#imports
import numpy as np
from keras.utils import np_utils
import pickle

#open text file with poems
text = (open("text_data/test_poetry4.txt").read()).lower()
# text = (open("text_data/test_poetry.txt").read()).lower()

#sort list of unique words in text
words = sorted(list(set(text.split(" "))))

#dictionary mapping words to ints
word_to_int = {word:n for n,word in enumerate(words)}

#dictionary mapping ints to words
int_to_word = {n:word for n,word in enumerate(words)}

#training and target lists
X,y = [],[]
text_length = len(text)
#length of string given to NN to make prediction
str_length = 15
print("Unique words:", len(fs))
print("Text length:", text_length)

#loop through text
for i in range(0, text_length - str_length, 1):
    #add a list of length str_length to training data
    X.append([word_to_int[c] for c in text[i : i + str_length]])
    #add the next word in the sequence to target list
    #y[n] will have the word than comes after x[n][str_length-1]
    #we want the NN to predict the next letter based on previous letters
    y.append(word_to_int[text[i + str_length]])

#reshape training data for the NN
X_2 = np.reshape(X, (len(X), str_length, 1))
#normalize the training data so that all values are between 0 and 1
X_2 = X_2 / float(len(words))
#convert Y to a one-hot array··
y_2 = np_utils.to_categorical(y)

with open('models/objects.pkl', 'wb') as f:
    pickle.dump([X, y, word_to_int, int_to_word, words], f)
