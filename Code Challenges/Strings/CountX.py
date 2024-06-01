def count_char_x(word, x):
    counter = 0
    for char in word:
        if char == x:
            counter += 1
    return counter

print(count_char_x("mississippi", "s"))
print(count_char_x("mississippi", "m"))
