#  Write a program to read through the mbox-short.txt
#  and figure out the distribution by hour of the day for each of the messages.
#  You can pull the hour out from the 'From ' line by finding the time
#  and then splitting the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts,
#  sorted by hour as shown below.

fileName = input("Enter a file: ")

if len(fileName) < 1 : fileName = 'mbox-short.txt'
fhand = open(fileName)
countHours = dict()
for line in fhand :
    if line.startswith('From') and not line.startswith('From:') :
        listString = line.strip().split()
        listTime = listString[5].split(':')
        hour = listTime[0]
        countHours[hour] = countHours.get(hour, 0) + 1

countHours = sorted(countHours.items())

for key, value in countHours :
    print(key,value)
