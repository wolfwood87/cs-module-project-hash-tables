import re
# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here

with open("ciphertext.txt") as f:
    cipher = f.read()


letter_freq = ["E", "T", "A", "O", "H", "N", "R", "I", "S", "D", "L", "W", "U", "G", "F", "B", "M", "Y", "C", "P", "K", "V", "Q", "J", "X", "Z"]

cipher_letters = {}

def build_cipher(s):
    for letter in s:
        letter = re.sub("[^A-Za-z]+", '', letter)
        if f"{letter}" in cipher_letters:
            cipher_letters[f"{letter}"] += 1
        elif letter != "":
            cipher_letters[f"{letter}"] = 1

build_cipher(cipher)
sorted_cipher = sorted(cipher_letters.items(), key=lambda x: x[1], reverse=True)

# print(sorted_cipher)
# print(sorted_cipher[0])

def decode(s):
    text = ""
    for letter in s:
        i = 0
        while i <= len(sorted_cipher) - 1:
            if f"{letter}" == sorted_cipher[i][0]:
                letter = letter_freq[i]
                i = len(sorted_cipher)
            i += 1
        text += letter
    return text

print(decode(cipher))


# print(decode("D"))