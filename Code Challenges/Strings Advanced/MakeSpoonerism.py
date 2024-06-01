def make_spoonerism(word1, word2):
    new_word = word2[0] + word1[1:] + " " + word1[0] + word2[1:]
    return new_word

print(make_spoonerism("Codecademy", "Learn"))
print(make_spoonerism("Hello", "world!"))
print(make_spoonerism("a", "b"))