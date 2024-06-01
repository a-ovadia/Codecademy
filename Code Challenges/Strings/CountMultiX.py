def count_multi_char_x(word, x):
    sub_string = word.split(x)
    return len(sub_string) - 1

print(count_multi_char_x("mississippi", "iss"))
print(count_multi_char_x("apple", "pp"))