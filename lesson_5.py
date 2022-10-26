# for i in range(1, 10):
#     for j in range(1, 10):
#         result = i * j
#         print(f"{j} * {i} = {result}", end="\t")
#     print()


mass = [
    [3, 2, 1],  
    [2, 3, 3],
    [0, 2, 5],
]

# for i in range(len(mass)):
    # print(mass[i])
#     for j in range(len(mass[i])):
#         if i == j:
#             mass[i][j] = 0
#         # print(mass[i][j], end=" ")
#         if i > j:
#             mass[i][j] = 1
#         if i < j:
#             mass[i][j] = 2
#     print(mass[i])



print(mass)

import random
gorod = ["bihkek", "Mockov", "New-York"]
city = random.choice(gorod)
popitky = 5
while True:
    if popitky == 0:
        break
    bukva = input("Vvedite bukvu: ")
    if bukva == city[0] or city[1] or city[2]:
        print("good!")
    else:
        popitky - 1
        print("ошибка!")

#     login = input("Введите своё имя: ")
#     password = input("Введите свой пароль: ")
#     if login == list1[0] and password == list1[1]:
#         print("добро пожаловать!")
#         break
#     elif attempts > 0:
#         print("неверно")
#         attempts -= 1
# def bank(m, n):
#     j = m = n * 0.10
#     return m

# m = int(input("Введите сумму: "))
# n = int(input("Введите сколько лет будет счет: "))
# k = bank(m, n)

# print(f"сумма через {n} лет составить- {k}")






