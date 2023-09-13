def delete_nth(order,max_e):
    result = []
    count ={}
    for num in order:
        if(num not in count):
            count[num] = 1
        else:
            count[num] += 1 #20:1
        if( count[num] <= max_e):
            result.append(num)

    return result

delete_nth([20,37,20,21], 1)