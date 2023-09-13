def add(num):
    def add_next(value):
        return add(num + value)
    
    add_next.value = num
    return add_next

addTwo = add(2)
print(add(1)(2)(3))
print(add(1)(2)(3)(4)(5)) 
print(addTwo (5) ) 