# Viết một chương trình có thể tính giai thừa của một số cho trước.
#  Kết quả được in thành chuỗi trên một dòng, phân tách bởi dấu phẩy.
#  Ví dụ, số cho trước là 8 thì kết quả đầu ra phải là 40320.

# #c1
#
# inp = input("Input an integer: ")
# try :
#     num = int(inp)
# except :
#     print("Please input an integer.")
#
# i = 1
# result = 1
#
# while i <= num :
#     result *= i
#     i += 1
# if num == 0 :
#     print(1)
# else :
#     print(result)

#c2
num = int(input("Nhap so can tinh giai thua: "))

def fact(number) :
    if number == 0 :
        return 1
    return number * fact(number - 1)

print(fact(num))
