def is_pangram(s):
    Character = "abcdefghijklmnopqrstuvwxyz"
    text = s.lower()
    for char in Character:
        if(char not in text):
            print (False)
            return False
    print (True)
    return True

