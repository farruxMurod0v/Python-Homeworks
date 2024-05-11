# with open("ismlar.txt", "w") as name:
#     for i in range(1, 5+1):
#         ism = input("ism kiriting: ")
#         name.write(f"{ism}\n")
#         print()

# sonlar = [
#     (24,56),
#     (55, -88),
#     (9, 98)
# ]
# sonlar = sorted (sonlar, key=lambda x: x[1])
# print(sonlar)


# sonlar = [0, 0, 5, 9, 69, 0, 87, 987, -98, 7]
# sonlar1 = []
# for i in sonlar:
#     if i != 0 :
#         sonlar1.append(i)
       
# zeros_count = len(sonlar) - len(sonlar1)
# sonlar1.extend([0] * zeros_count)
# print(sonlar1)


sonlar = [0, 0, 5, 9, 69, 87, 7]
for i in sonlar:
    if i == 0:
        sonlar.insert(-1, i)

print(sonlar)


