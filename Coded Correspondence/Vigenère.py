# define our alphabet
alphabet = "abcdefghijklmnopqrstuvwxyz"


# Generate a Vigenere keyword phrase based on the length of the entire message
def keyword_phrase(keyword, message_length):
    phrase = ""
    for num in range(message_length):
        phrase += keyword[num % len(keyword)]
    return phrase

# Return the position of a character in the alphabet
def find_position_in_alphabet(word):
    return alphabet.find(word)

# Vigenere alg.
# Inputs: message -> Type: Str -> text to encrypt or decrypt
#         keyboard -> Type: Str -> key for Vigenerge
#         decrypt -> Type Bool -> Default True to decrypt, False to Encrypt
def vig(message, keyword, decrypt=True):
    keyphrase = keyword_phrase(keyword, len(message))
    return_message = ""
    counter = 0
    for char in message:
        if char in alphabet:
            message_index = find_position_in_alphabet(char)
            key_index = find_position_in_alphabet(keyphrase[counter])
            if not decrypt: key_index = key_index * -1
            counter += 1
            return_message += alphabet[(message_index + key_index) % 26]
        else:
            return_message += char
    return return_message


# Codecademy test calls
message = "txm srom vkda gl lzlgzr qpdb? fepb ejac! ubr imn tapludwy mhfbz cza ruxzal wg zztcgcexxch!"
key = "friends"
decrypted_message = "you were able to decode this? nice work! you are becoming quite the expert at crytography!"
print(vig(decrypted_message.lower(), key, False))
print(vig(message.lower(), key))