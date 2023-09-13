def solution(args):
    result = []
    i = 0

    while i < len(args):
        start = args[i]
        while i < len(args) - 1 and args[i + 1] == args[i] + 1:
            i += 1
        end = args[i]
        
        if end - start >= 2:
            result.append(f"{start}-{end}")
        else:
            result.extend(map(str, range(start, end + 1)))

        i += 1
        
    return ','.join(result)


args = [-10, -9, -8, -6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20]
formatted_output = solution(args)
print(formatted_output)  
