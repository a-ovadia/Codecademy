def x_length_words(sentence, x):
    split_sentence = sentence.split(" ")
    for word in split_sentence:
        if len(word) < x:
            return False
    return True
print(x_length_words("i like apples", 2))
print(x_length_words("he likes apples", 2))