

def caesar_encode(plain_text, shift):
    cipher_text = ""
    for c in plain_text:
        c_encode = ord(c) + shift
        if(c_encode > ord('z')):
            c_encode = c_encode % 26
        c_encode = chr(c_encode)
        cipher_text += c_encode
    return cipher_text