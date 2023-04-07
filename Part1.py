#Python Lists Check pt1------------------------------------------------------------------------

FavFood = ["pizza", "icecream", "cheezburger", "burgir", "burito", "lays", "dorito", "dogfood"]
print(FavFood[2])
FavFood.append("tacos")
#print(FavFood)

size = 0
for i in FavFood:
    size += 1

print ("the list size is, ", size)

print(FavFood)
