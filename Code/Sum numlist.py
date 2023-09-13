def sumnum(n):
    numlist = [int(x) for x in str(n)]
    total = sum(int(x) for x in numlist)
    while total > 9:
        numlist = [int(x) for x in str(total)]
        total = sum(int(x) for x in numlist)
    return total
sumnum(493193)