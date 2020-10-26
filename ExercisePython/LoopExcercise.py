# Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'.
# Once 'done' is entered, print out the largest and smallest of the numbers.
# If the user enters anything other than a valid number catch it with a try/except
# and put out an appropriate message and ignore the number. Enter 7, 2, bob, 10, and 4
# and match the output below.

largestNumber = -1
smallestNumber = None
while True :
    inputNumber = input("Input an interger number: ")
    if inputNumber == 'done' :
        break
    try :
        inputNumberInt = int(inputNumber)
    except :
        print("Invalid input")
        continue
    if largestNumber < inputNumberInt :
        largestNumber = inputNumberInt
    if smallestNumber is None :
        smallestNumber = inputNumberInt
    elif smallestNumber > inputNumberInt :
        smallestNumber = inputNumberInt

if smallestNumber is None or largestNumber == -1 :
    print("You still don't input any numbers")
else :
    print("Maximum is", largestNumber)
    print("Minimum is", smallestNumber)
