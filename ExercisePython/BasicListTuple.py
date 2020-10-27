# Viết chương trình chấp nhận một chuỗi số, phân tách bằng dấu phẩy từ giao diện điều khiển,
 # tạo ra một danh sách và một tuple chứa mọi số.
#
# Ví dụ: Đầu vào được cung cấp là 34,67,55,33,12,98 thì đầu ra là:
#
# ['34', '67', '55', '33', '12', '98']
# ('34', '67', '55', '33', '12', '98')

values = input("Nhap vao mot chuoi so: ")

list = values.split(",")
t = tuple(list)

print(list)
print(t) #tuple
