def every_other_letter(word):
    every_other = ""
    for char in range(len(word)):
        if char % 2 == 0:
            every_other += word[char]
    return  every_other


print(every_other_letter("Codecademy"))
print(every_other_letter("Hello world!"))
print(every_other_letter(""))