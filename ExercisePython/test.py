#
# d = 1
# x = 0
# while d != 0 :
#     d = (396 * x + 1) % 283
#     e = (396 * x + 1) / 283
#     x += 1
# print("e: ", e, "d: ", d)

# plaintext = [0x04, 0x89, 0x1F, 0x1F, 0x1F, 0x1F, 0x1F, 0x1F, 0x1F, 0x1F, 0x1F, 0x1F, 0x1F, 0x1F, 0x04, 0x89]
# key = [0x04, 0x89, 0xF1, 0xF1, 0xF1, 0xF1, 0xF1, 0xF1, 0xF1, 0xF1, 0xF1, 0xF1, 0xF1, 0xF1, 0x04, 0x89]
#
# for i in range(0,16):
#     print(hex(plaintext[i] ^ key[i]))
# print(hex(0xC6 ^ 0x78 ^ 0x28 ^ 0x63))
# The top 10 most common words

# fhand = open('mbox-short.txt')
#
# countDic = dict()
# for line in fhand :
#     words = line.strip().split()
#     for word in words :
#         countDic[word] = countDic.get(word, 0) + 1
#
# lst = list()
#
# for key, value in countDic.items() :
#     reverse = (value, key)
#     lst.append(reverse)
#
# lst = sorted(lst, reverse = True)
#
# for value, key in lst[:10] :
#     print(key, value)
x = 122
print("%04d"%x)
