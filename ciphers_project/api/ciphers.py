

def caesar_encode(plain_text, shift):
    cipher_text = ""
    for c in plain_text:
        if c.isalpha():
            if c.islower():
                c_encode = (ord(c) - ord('a') + shift) % 26 + ord('a')
            else:
                c_encode = (ord(c) - ord('A') + shift) % 26 + ord('A')
            c_encode = chr(c_encode)
        else:
            c_encode = c
        cipher_text += c_encode
    return cipher_text