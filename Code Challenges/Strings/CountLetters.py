def unique_english_letters(word):
    unique_letters = ""
    for char in word:
        if not char in unique_letters:
            unique_letters += char
    return len(unique_letters)

print(unique_english_letters("mississippi"))
print(unique_english_letters("Apple"))