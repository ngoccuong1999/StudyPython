from collections import Counter
fhand = open('mbox-short.txt')
string = fhand.read()
list = []
list = string.split()
count = Counter(list)
print(count)
print(count.most_common(1))
