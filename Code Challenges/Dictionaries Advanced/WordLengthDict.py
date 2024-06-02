def word_length_dictionary(words):
    new_dict = {}
    for entry in words:
        new_dict[entry] = len(entry)
    return new_dict

print(word_length_dictionary(["apple", "dog", "cat"]))
# should print {"apple":5, "dog": 3, "cat":3}
print(word_length_dictionary(["a", ""]))
# should print {"a": 1, "": 0}