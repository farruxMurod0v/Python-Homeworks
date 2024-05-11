shaharlar = {"Toshkent", "Samarqand", "Buxoro", "Andijon", "Xiva"}
input_shahar = input("Shahar nomini kiriting: ")
if input_shahar in shaharlar:
    shaharlar.remove(input_shahar)
    print("Setdan", input_shahar, "o'chirildi")
print(" qolgan shaharlar :", shaharlar)
