def no_dups(s):
    # Your code here
    sentence_arr = []
    sentence = ""
    words = s.split()
    i = 0
    while i < len(words):
        if words[i] in sentence_arr:
            i += 1
        else:
            sentence_arr.append(words[i])
            if i != len(words) - 1:
                a = i+1
            i += 1
    a = 0
    while a < len(sentence_arr):
        if a < len(sentence_arr)-1:
            sentence += sentence_arr[a] + " "
        else:
            sentence += sentence_arr[a]
        a += 1
    return sentence





if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))