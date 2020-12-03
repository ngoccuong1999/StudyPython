
#Khởi tạo S ban đầu bằng cách cho giá trị bằng thứ tự bình  thường sễ là 256 phần tử từ 0 --> 255
#T tạm thời chính là key ban đầu lặp lại sao cho = số phần từ với S
# plaintext = [1 2 0 1]
#key = [0 1] == > s và t ban đầu như bên dưới
s = [0, 1, 2, 3, 4, 5, 6, 7]
t = [0, 4, 0, 1, 0, 4, 0, 1]

#b1: Hoán đổi S initial permutation bang cong thức như dưới
j = 0;
for i in range(0, 8) :
    j = (j + s[i] + t[i]) % 8
    s[i], s[j]  = s[j], s[i]

print("Initial permuatation S = ", s, end = "\n\n") # s sau khi hoán đổi

#b2: Sinh giá trị gamma chính là k với mỗi k sẽ xor với plaintext tương ứng để sinh ra ciphertext
#while(true) nghĩa là sẽ sinh k cho đến khi nào đủ hêt cho plaintext
# bước này là stream generation hay pseudo-random generation algorithm (PRGA). The PRGA is below hay key stream
p = [0, 4, 0, 1]
i, j, count = 0, 0, 0
while count < 4 :
    i = (i + 1) % 8
    j = (j + s[i]) % 8
    s[i], s[j] = s[j], s[i]
    t = (s[i] + s[j]) % 8
    k = s[t]
    print("K: ", k)
    print("k xor plaintext")
    p[count] = k ^ p[count]
    print(p[count],  end = "\n\n")
    count += 1


print("ciphertext:", p)
