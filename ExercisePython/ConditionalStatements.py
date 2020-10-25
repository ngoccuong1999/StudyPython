# #Write a program to prompt the user for hours
# #   and rate per hour using input to compute gross pay.
# Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours.
# # Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75).
# # You should use input to read a string and float() to convert the string to a number.
# # Do not worry about error checking the user input
# # - assume the user types numbers properly.

hours = input("Input hours:")
ratePerHours = input("Input rate per hours: ")

try:
    hoursFloat = float(hours)
except:
    print("Input wrong hours")
    quit()
try:
    ratePerHoursFloat = float(ratePerHours)
except:
    print("Input wrong rate per hours")
    quit()
if hoursFloat <= 40:
    pay = hoursFloat * ratePerHoursFloat
else:
    pay = hoursFloat * ratePerHoursFloat * 1.5
print(pay)
