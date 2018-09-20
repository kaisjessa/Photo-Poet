text = (open("text_data/test_poetry4.txt").read())#.lower()

words = sorted(list(set(text.split(" "))))
word_to_int = {word:n for n,word in enumerate(words)}
int_to_word = {n:word for n,word in enumerate(words)}
text_length = len(text)
print("Unique words:", len(words))
print("Text length:", text_length)

chars = sorted(list(set(text)))
char_to_int = {char:n for n,char in enumerate(chars)}
int_to_char = {n:char for n,char in enumerate(chars)}
print("Unique chars:", len(chars))
print("Text length:", text_length)