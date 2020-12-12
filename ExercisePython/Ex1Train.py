import re

username = input("Enter username: ")
password = input("Enter password separated by a comma: ")

listPassword = password.split(',')
listValidPassword = list()
regex = "^\s*(?=.*[a-z]+)(?=.*[0-9]+)(?=.*[A-Z]+)(?=.*[$#@]+)[a-zA-Z0-9$#@]{6,12}$"
regex1 = "[a-zA-Z0-9$#@]{6,12}"
for password1 in listPassword :
    print(password1)
    if re.search(regex, password1) :
        print("1")
        listValidPassword.append(password1)

result = ",".join(listValidPassword)
print("List valid: ", listValidPassword)
print("result:", result)
