# Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages.
# The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail.
# The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file.
# After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.
# fhand = open('mbox-short.txt')
#
# list = list()
# dictionary = dict()
# for line in fhand :
#     if line.startswith('From') and not line.startswith('From: ') :
#         listTemp = line.strip().split()
#         dictionary[listTemp[1]] = dictionary.get(listTemp[1], 0) + 1
#
# bigCount = None
# bigWord = None
#
# for word in dictionary :
#     count = dictionary[word]
#     if bigCount == None or bigCount < count :
#         bigCount = count
#         bigWord = word
#
#
# print(bigWord, bigCount) c1

from collections import Counter

fhand = open('mbox-short.txt')

list = list()
for line in fhand :
    if line.startswith('From') and not line.startswith('From: ') :
        listTemp = line.strip().split()
        list.append(listTemp[1])

count = Counter(list)
print(count.most_common(1))
