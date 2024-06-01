def substring_between_letters(word, start,end):
    if not start in word or not end in word:
        return word
    return word[word.find(start)+1:word.find(end)]

print(substring_between_letters("apple", "p", "e"))
print(substring_between_letters("apple", "p", "c"))
