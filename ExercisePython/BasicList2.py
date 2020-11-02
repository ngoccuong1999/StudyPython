# Open the file mbox-short.txt and read it line by line.
#  When you find a line that starts with 'From ' like the following line:
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# You will parse the From line using split() and print out the second word in the line
#  (i.e. the entire address of the person who sent the message).
#  Then print out a count at the end.
# Hint: make sure not to include the lines that start with 'From:'.
# Also look at the last line of the sample output to see how to print the count.

fhand = open('mbox-short.txt')
count = 0
listAddress = list()
for line in fhand :
    if line.startswith('From') :
        list = line.split()
        if len(list) > 4 :
            count += 1
            listAddress.append(list[1])


for element in listAddress :
    print(element)

print("There were", count, "lines in the file with From as the first word")
