def no_dups(s):
    word_list = s.split()
    word_dict = {}

    for word in word_list:
        if word in word_dict.keys():
            pass
        else:
            word_dict[word] = word
    
    new_word_list = list(word_dict.keys())

    sentence = ' '.join(new_word_list)

    return sentence


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))