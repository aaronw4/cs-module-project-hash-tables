import random

# Read in all the words in one go
with open("C:/Users/aaron/Git/cs-module-project-hash-tables/applications/markov/input.txt") as f:
    words = f.read()

word_list = words.split()
word_dict = {}

# TODO: analyze which words can follow other words
for i in range(len(word_list)-1):
    if word_list[i] in word_dict.keys():
        word_dict[word_list[i]].append(word_list[i+1])
    else:
        word_dict[word_list[i]] = [word_list[i+1]]

# TODO: construct 5 random sentences

for i in range(5):
    key_list = list(word_dict)
    word = random.choice(key_list)
    endings = ['.', '?', '!']
    sentence_list = []

    while word[0].islower():
        word = random.choice(key_list)

    sentence_list.append(word)

    while word[-1] not in endings:
        word = random.choice(word_dict[word])
        sentence_list.append(word)
        if len(word) > 1:
            if word[-2] in endings:
                break

    sentence = ' '.join(sentence_list)
    print(sentence)