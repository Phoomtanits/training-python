from functools import reduce

def persistence(n):
    count = 0
    while(n >= 10): 
        n_str = str(n)
        numList = [int(digit) for digit in n_str]
        result = reduce(lambda x,y:x*y,numList) #reduce คือการคูณตัวใน array ทั้งหมด
        n = result
        count += 1
    print(count)

persistence(0)
