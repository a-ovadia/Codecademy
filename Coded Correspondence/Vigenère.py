# define our alphabet
alphabet = "abcdefghijklmnopqrstuvwxyz"


def keyword_phrase(keyword, message_length):
    phrase = ""
    for num in range(message_length):
        phrase += keyword[num % len(keyword)]
    return phrase

def find_position_in_alphabet(word):
    return alphabet.find(word)

def vig_decrypt(message, keyword):
    keyphrase = keyword_phrase(keyword, len(message))
    decrypted_message = ""
    counter = 0
    for char in message:
        if char in alphabet:

            #message_index = alphabet.find(char[0])
            message_index = find_position_in_alphabet(char)
            key_index = find_position_in_alphabet(keyphrase[counter])
            counter += 1
            #decrypted_index = (message_index + key_index) % 26
            #print("Message Index: {}, Key Index: {},  Decrypted_Index = {}".format(message_index, key_index, decrypted_index))
            decrypted_message += alphabet[(message_index + key_index) % 26]
        else:

            decrypted_message += char
    return decrypted_message


def vig_encrypt(message, keyword):
    keyphrase = keyword_phrase(keyword, len(message))
    encrypted_message = ""
    counter = 0
    for char in message:
        if char in alphabet:

            #message_index = alphabet.find(char[0])
            message_index = find_position_in_alphabet(char)
            key_index = find_position_in_alphabet(keyphrase[counter])
            counter += 1
            #decrypted_index = (message_index + key_index) % 26
            #print("Message Index: {}, Key Index: {},  Decrypted_Index = {}".format(message_index, key_index, decrypted_index))
            encrypted_message += alphabet[(message_index - key_index) % 26]
        else:

            encrypted_message += char
    return encrypted_message

message = "txm srom vkda gl lzlgzr qpdb? fepb ejac! ubr imn tapludwy mhfbz cza ruxzal wg zztcgcexxch!"
key = "friends"
decrypted_message = "you were able to decode this? nice work! you are becoming quite the expert at crytography!"
print(vig_decrypt(message.lower(), key))
print(vig_encrypt(decrypted_message, key))
