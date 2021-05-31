#De  khong noi ro la cho san list interger hay la minh nhap vao nen
#em nhap vao do dai va nhap vao list
#listInteger = [64, 25, 12, 22, 11]
listInteger = []
testInput = 1
while testInput != 0 :
    try:
        length = int(input("Nhap do dai cua list: "))
        while length < 0:
            print("Nhap sai!!! Vui long nhap vao mot so tu nhien > 0")
            length = int(input("Nhap do dai cua list: "))
        testInput = 0
    except:
        print("Nhap sai!!! Vui long nhap vao mot so tu nhien > 0")
testInput = 1

while testInput != 0 :
    try:
        print("Nhap phan tu cua mang")
        for i in range(length):
            listInteger.append(int(input('')))

        testInput = 0
    except:
        print("Nhap sai!!! Vui long nhap vao mot so tu nhien ")
        listInteger = []

print("Input: A = ", listInteger)
#array sorted
resultList = []
for i in range(len(listInteger)):
    min = i
    for j in range(i + 1, len(listInteger)) :
        if listInteger[min] > listInteger[j]:
            min = j
    #them  min vao array sorted
    resultList.append(listInteger[min])
    #tim vi tri cua min trong array unsorted
    #swap vi tri
    listInteger[i], listInteger[min] = listInteger[min], listInteger[i]
#In  ra theo yeu cau
print("Sorted array ")
for i in resultList :
    print(i)
