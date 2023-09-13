def make_readable(seconds):
    HH = 0
    MM = 0
    SS = 0
    for i in range (seconds , 0 , -1):
        if( seconds >= 3600):
            HH += 1
            seconds -= 3600
        elif( seconds >= 60):
            MM += 1
            seconds -= 60
        else:
            SS = seconds
            break
    if(HH <=9):
        HH = f"0{HH}"
    if(MM <=9):
        MM = f"0{MM}"
    if(SS <=9):
        SS = f"0{SS}"

    sum = f"{HH}:{MM}:{SS}"
    print(sum)
    return sum

make_readable(60)
