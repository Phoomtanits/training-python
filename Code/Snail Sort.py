def snail(snail_map):
    result = []
    while(snail_map):
        result += snail_map.pop(0)
        print("1 : ",result)
        if(snail_map and snail_map[0]):
            for row in snail_map:
                result.append(row.pop())
                print("2 : ",result)
        if(snail_map):
            result += snail_map.pop()[::-1]
            print("3 : ",result)
        if(snail_map and snail_map[0]):
            for row in snail_map[::-1]:
                result.append(row.pop(0))
                print("4 : ",result)
    return result


array = [[1,2,3],
         [4,5,6],
         [7,8,9]]
snail(array)