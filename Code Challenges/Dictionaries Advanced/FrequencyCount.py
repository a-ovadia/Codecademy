def frequency_dictionary(words):
    new_dict = {}
    for entry in words:
        if entry not in new_dict:
            new_dict[entry] = 0
        new_dict[entry] += 1

    return new_dict


print(frequency_dictionary(["apple", "apple", "cat", 1]))
# should print {"apple":2, "cat":1, 1:1}
#print(frequency_dictionary([0,0,0,0,0]))
# should print {0:5}

