# def add (*summa):
#     total = 0
#     for sum in summa:
#         total+=sum
#     return total
    
# print(add(49,5497,649))


def print_adress(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_adress(street = "manaviyat",
             city = "oltiariq",
             state = "Fergana",
             number = "100")