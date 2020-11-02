# Open the file romeo.txt and read it line by line.
# For each line, split the line into a list of words using the split() method.
# The program should build a list of words.
# For each word on each line check to see if the word is already in the list and if not append it to the list.
# When the program completes, sort and print the resulting words in alphabetical order.
fhand = open('romeo.txt')
listWord = list()

for line in fhand :
    list = line.rstrip().split()
    for word in list:
        if not word in listWord:
            listWord.append(word)

listWord.sort()
print(listWord)
