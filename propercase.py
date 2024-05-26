def fix_caps_lock(word):
    if word.isupper() or (word[1:].isupper() or word[0].islower()):
        return word.swapcase()
    else:
        return word
string=input()
print(fix_caps_lock(string))
