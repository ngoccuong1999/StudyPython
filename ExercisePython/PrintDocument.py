# Python có nhiều hàm được tích hợp sẵn, nếu không biết cách sử dụng nó
# , bạn có thể đọc tài liệu trực tuyến hoặc tìm vài cuốn sách.
# Nhưng Python cũng có sẵn tài liệu về hàm cho mọi hàm tích hợp trong Python.
# Yêu cầu của bài tập này là viết một chương trình để in tài liệu về một số hàm Python được tích hợp sẵn như abs(), int(), input()
# và thêm tài liệu cho hàm bạn tự định nghĩa.

print("Abs: ")
print(abs.__doc__)

print("Int: ")
print(int.__doc__)
print("Input: ")
print(input.__doc__)

def square(num) :
    return num ** 2
print("Square: ")
print(square.__doc__)
