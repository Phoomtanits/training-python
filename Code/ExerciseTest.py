def MaxValueOfTwoNum():
    x = int(input("Value Num X : "))
    y = int(input("Value Num Y : "))
    if(x > y):
        print("Max Value is X : ",x)
    else:
        print("Max Value is Y : ",y)
    
def MaxValueOfFourNum():
    num_list = []
    i = 1
    sum = 0
    for i in range(4):
        num = int(input("Value of Number %d : "  % (i + 1)))
        num_list.append(num)
        
    count = len(num_list)
    for j in range(count):
        if  num_list[j] > sum :
            sum = num_list[j]
    print("Max Value is : ",sum)
    
def SayHappy():
    text = input("Do you want a Happy Birthday? (y/n) : y")
    if(text == "y"):
        print("Happy Birthday!")
    else:
        print("Okay then. Goodbye!")
           
def Rectangle():
    hight = float(input("INPUT HIGHT : "))
    width = float(input("INPUT WIDTH : "))
    if(hight <= 0 or width <= 0):
        print("Input us invalid!")
    else:
        print("Rectangle Area : ",hight*width)
        
# MaxValueOfTwoNum()
# MaxValueOfFourNum()
# SayHappy()     
# Rectangle()