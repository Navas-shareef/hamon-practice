def panagram(sentence):
    key='abcdefghijklmnopqrstuvwxyz'
    sentence=sentence.lower()
    for i in key:
        if i in sentence:
            pass
        else:
            return False
    return True        


sentence=input("enter a centence to check whether it is panagram or not\n")
result=panagram(sentence)
if result:
    print('it is a panagram')
else:
    print('it is not panagram')    

