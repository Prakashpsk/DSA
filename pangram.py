def panagram(sen):
    alphabet="abcdefghijklmnopqrstuvwxyz"
    for char in alphabet:
        if char not in sen.lower():
            return False
    return True
sen= "the qucik brown fox jumps over the lazy dog"
if panagram(sen) == True:
    print("yes")
else:
    print("No")