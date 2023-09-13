# def solution(s):
#     size = 2
#     item = []
#     itemCount = len(s)
#     if(itemCount == 0):
#         print(item)
#     elif(itemCount % 2 != 0):
#         addChar = "_"
#         char = s + addChar
#         item = [char [i:i+size] for i in range (0,len (char) , size)]
#         print(item)
#     else:
#         item = [s [i:i+size] for i in range (0,len (s) , size)]
#         print(item)
#     return item

def solution(s):
    pairs = []
    for i in range(0, len(s), 2):
        if i + 1 < len(s):
            pairs.append(s[i:i+2])
        else:
            pairs.append(s[i] + '_')
    print(pairs)
    return pairs

solution('')