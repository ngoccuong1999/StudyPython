smallestValue = None

for i in [1, 5, 6, 7, 10, 15, 16]:
    if smallestValue is None:
        smallestValue = i
    elif smallestValue > i :
        smallestValue = i

print("Smallest Value:", smallestValue)
