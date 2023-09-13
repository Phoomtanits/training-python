def cakes(recipe, available):
    number = float('inf')
    for i , amount in recipe.items():
        if i not in available or available[i] < amount :
            return 0
        number = min(number,available[i] // amount)
    return number



cakes({"flour": 500, "sugar": 200, "eggs": 1}, {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200})