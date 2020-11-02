#  Write a program that prompts for a file name,
#  then opens that file and reads through the file, looking for lines of the form:
# X-DSPAM-Confidence:    0.8475
# Count these lines and extract the floating point values from each of the lines and
#  compute the average of those values and produce an output as shown below.
#  Do not use the sum() function or a variable named sum in your solution.


fhand = open(input("Enter a file name: "))

count = 0
total = 0
for line in fhand :
    if 'X-DSPAM-Confidence' in line :
        count += 1
        start = line.find(':')
        total += float(line[start+1:].strip())


print("Average spam confidence:", total / count)
