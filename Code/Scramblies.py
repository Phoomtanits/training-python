def scramble(s1, s2):
    character = s2.lower()
    count = len(character)
    for char in character:
        if(char not in s1):
            break
        else:
            s1 = s1.replace(char,'',1)
            count -= 1
    if(count == 0):
        return True
    else:
        return False
    
# def scramble(str1, str2):
#     char_count = [0] * 26  
    
#     for char in str1:
#         char_count[ord(char) - ord('a')] += 1
    
#     for char in str2:
#         if char_count[ord(char) - ord('a')] == 0:
#             return False
#         char_count[ord(char) - ord('a')] -= 1
    
#     return True


    
scramble('rkqodlw', 'world')
scramble('cedewaraaossoqqyt', 'codewars')
scramble('katas', 'steak')
scramble('scriptjava', 'javascript')
scramble("kssrteiyhztrxvafd","eafsyfz")
