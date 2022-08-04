def letter_count(sentence):
    dic = {

    }
    for letter in sentence:
        if letter not in dic:
            dic[letter] = list(sentence).count(letter)
    return dic
