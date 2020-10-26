# Viết chương trình tìm tất cả các số chia hết cho 7 nhưng không phải bội số của 5,
# nằm trong đoạn 2000 và 3200 (tính cả 2000 và 3200).
# Các số thu được sẽ được in thành chuỗi trên một dòng, cách nhau bằng dấu phẩy.

# #cach 1
# list = []
# i = 2000
# while (i >= 2000) and (i <= 3200) :
#     if i % 7 == 0 :
#         if i % 5 != 0 :
#             list.append(i)
#     i = i + 1
#
# print(list)
#cach 2
list = []
for i in range(2000, 3200) :
    if (i % 7 == 0) and (i % 5 != 0) :
        list.append(str(i))

print(','.join(list))
