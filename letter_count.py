from operator import le


def letter_count(sentence):
    dic = {

    }
    for letter in sentence.replace(" ", ''):
        if letter not in dic:
            dic[letter] = list(sentence).count(letter)
    return dic


print(letter_count("navas shareef"))
