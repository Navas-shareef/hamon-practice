import string


def panagram(sentence):

    sentence = sentence.lower()
    for letter in string.ascii_lowercase:
        if letter not in sentence:

            return False
    return True


# if __name__ == '__main__':
