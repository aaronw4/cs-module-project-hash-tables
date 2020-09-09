def word_count(s):
    bad_chars = [';', ':', '&', "*", '"', ',', '.', '-', '+', '=', '/', "\\", '|', '[', ']', '{', '}', '(', ')', '^'] 
    
    for i in bad_chars:
        s = s.replace(i, '')
        s = s.lower()
    
    array = s.split()
    
    dic = {}

    for i in array:
        if i not in dic.keys():
            dic[i] = 1
        else:
            number = dic[i]
            number += 1
            dic[i] = number
    print(dic)
    return dic



if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))