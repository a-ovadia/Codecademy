def reverse_string(word):
    reverse = ""
    for num in range(len(word)):
        reverse += word[-num -1 ]

    return reverse

print(reverse_string("Codecademy"))
print(reverse_string("Hello world!"))
print(reverse_string(""))