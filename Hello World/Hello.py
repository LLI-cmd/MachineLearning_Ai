italians = ["dish1", "dish2", "dish3"]
nigerian = ["dish4", "dish5", "dish6"]
ghana = ["dish7", "dish8", "dish9"]

num = input("enter a dish name ")
#num = int(num)#
if num in italians:
    print("italian dish")
elif num in nigerian:
    print("nigerian dish")
elif num in ghana :
    print("ghana dish")
else:
    print("unknown dish")

for dish in ghana:
    print(dish)
