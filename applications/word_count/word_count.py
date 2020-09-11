import re

def word_count(s):
    hash_count = {}
    # Your code here
    words = s.split()
    for word in words:
        word = re.sub("[^A-Za-z0-9']+", '', word)
        lower = word.lower()
        if f"{lower}" in hash_count:
            hash_count[f"{lower}"] += 1
        elif word != "":
            hash_count[f"{lower}"] = 1
    return hash_count



if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))