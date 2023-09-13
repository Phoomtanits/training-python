def permutations(s):
    if len(s) == 1:
        return [s]
    
    permutations = set()  
    
    for i, char in enumerate(s):
        remaining_chars = s[:i] + s[i+1:]
        sub_permutations = permutations(remaining_chars)
        for sub_perm in sub_permutations:
            permutations.add(char + sub_perm)
    
    return list(permutations)


print(permutations('a'))   # ['a']
print(permutations('ab'))  # ['ab', 'ba']
print(permutations('abc')) # ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
