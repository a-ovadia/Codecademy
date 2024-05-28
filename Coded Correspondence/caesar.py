alphabet = "abcdefghijklmnopqrstuvwxyz"

def caesar_decrypt(message, offset):
    decrypted_message = ""
    for letter in message:
        if letter in alphabet:
            position = alphabet.find(letter)
            decrypted_message += alphabet[(position + offset) % 26]
        else: decrypted_message += letter
    return decrypted_message

def caesar_encrypt(message, offset):
    encrypted_message = ""
    for letter in message:
        if letter in alphabet:
            position = alphabet.find(letter)
            encrypted_message += alphabet[(position - offset) % 26]
        else: encrypted_message += letter
    return encrypted_message

encrypted = "xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!"

print(caesar_decrypt(encrypted, 10))
my_response = "Hi! Yes I was able to decode the message. Please see this message"
print(caesar_encrypt(my_response, 10))

# Unknown offset
coded_message = "vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl hulhexmx. px'ee atox mh kxteer lmxi ni hnk ztfx by px ptgm mh dxxi hnk fxlltzxl ltyx."
for num in range(len(alphabet)):
    print("Offet: {}  + Message: {}".format(num, caesar_decrypt(coded_message, num)))

# Found offset value = 7