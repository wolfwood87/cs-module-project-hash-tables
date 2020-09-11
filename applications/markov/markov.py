import random

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()

hash_words = {}
start_words = []
end_words = []
# TODO: analyze which words can follow other words
# Your code here
def construct_data(items):
    i = 0
    items = items.split()
    while i < len(items) - 1:
        if items[i].isupper() or items[i][0] == '"':
            start_words.append(items[i])
        elif items[i][0] == '"' and items[i][1].isupper():
            start_words.append(items[i])
        if items[i][len(items[i])-1] == '?' or items[i][len(items[i])-1] == '.' or items[i][len(items[i])-1] == '!':
            end_words.append(items[i])
        elif items[i][len(items[i])-1] == '"':
            if items[i][len(items[i])-2] == '?' or items[i][len(items[i])-2] == '.' or items[i][len(items[i])-2] == '!':
                end_words.append(items[i])
        if items[i] in hash_words:
            hash_words[f"{items[i]}"].append(items[i+1])
        else:
            hash_words[items[i]] = [items[i+1]]
        i += 1
    

construct_data(words)

# TODO: construct 5 random sentences
# Your code here
def random_sentence(words):
    sentence = []
    word = random.choice(start_words)
    while word not in end_words:
        sentence.append(word)
        print(word, end=" ")
        word = random.choice(hash_words[word])
    print(word)
    
random_sentence(hash_words)
