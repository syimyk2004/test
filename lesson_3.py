# dict словари


# dicts = {
#     "name": "nazgul",
#     "age": 12,
#     "subjekts": {
#         "python": 8.14,
#         "math": 89,
#     },
# }

# print(dicts["name"])

# for i in dicts:
#     if type(dicts[i]) == dict:
#         for j in dicts[i]:
#             print(dicts[i][j])




# python = {
#     "aliza": 78,
#     "zabira": 77,
#     "smanaly": 90,
#     "aman": 66,
#     "nurlan": 88

# }

# counter = 0

# for i in python.values():
#     counter += i
# print(counter / len(python))
# python["ilgis"] = 100

# print(sum(python.values()) / len(python))
# print(python.items())
# print(python.keys())
# print(python.values())
    # print(i)


# for key, value in python.items():
#     print(i)

# # print(dir(dict))

# hackerrank
# leetcode

# dicus = dict()
# print(len(python))


# methods
# print(python.get("nurlan"))

# languahes = ["python", "java", "go"]

# dict_lang = dict.fromkeys(languahes, 9)

# print(dict_lang)


# python3 = python.copy
# python3["anan"]  = 55

# print(python.setdefault("zamira", 5))

# python.clear()
# print(python)

# python2 = {
#     "arsen": 56,
#     "aziz": 88,
#     "ilgiz": 96,
# }


# python.update(python2)
# print(python)
#                   задача 
# dict_product = {}

# while True:
#     product_price = input("Введите товар Введите цену:  ")
#     if product_price == "stop":
#         break
#     key, value = product_price.strip().split()
#     dict_product[key] = int(value)  / 83
#     print(dict_product)

# def palindrom(filename):
#     if filename == filename(reverse=True):
#         return "yes"
#     else:
#         False
# print(palindrom("111"))



# def check_digit(a):
#     if a < 10:
#         return "Меньше 10"
#     elif a >= 10 and a < 100:
#         return "Число в промежутке между 10 и 100"
#     else:
#         return "Число больше 100"


# def palindrom(str_value):
#     if str_value == str_value[:: -1]:
#         return "this is polindrom!!!"
#     else:
#         return "No"


# def bank(m, n):
#     for i in range(10):




# student = {
#     "surname": "Chingizov",
#     "subjekts": [
#         {"name": "math", "grade": 80},
#         {"name": "programmer", "age": 55},
#     ]


# }


# # set collection
# sets = {
# }
# sets = set()

# proffesion = {"backend", 12, (1, 3, 3), [3, 5, 6]}
# # for i in proffesion:
# #     print(i)
# lest_set = list(proffesion)
# print(lest_set)



# cities = {"Tokio", "Bishkek"}
# town = {"asdflk", "narun"}

# inter = cities.intersection(towns)
# cities.intersection_update(towns)
# cities.symmetric_difference(towns)
# cities.symmetric_difference_update(towns)

# print(cities.issubset(towns))
# print(cities.issuperset(towns))
# print(cities.isdisjoint(town))


# print(dir(cites))

# cities.add("Tokio")
# cities.clear()
# cities.discard("Bishkek")
# cities.remove("Bishkek")
# print()







# student = {
#     "name": "Aman",
#     "age": 18,
#     "year": None,
#     "subjekts": {
#         "math": (80, 47, 68, 100),
#         "python": (67, 88, 97, 82),
#         "html": (67, 80, 97, 88),
#         "css": (67, 88, 91, 88),
#     },
#     "total": None
# }

# # # print(student)

# student["year"] = 2022 - student["age"]
# for key, value in  student["subjekts"].items():
#     student["subjekts"][key] = sum(value) / len(value)

# student['total'] = sum(student["subjekts"].values()) / len(student["subjekts"])
# print(student)


# for i in python.values():
#     counter += i
# print(counter / len(python))
# python["ilgis"] = 100

# print(sum(python.values()) / len(python))
# print(python.items())
# print(python.keys())
# print(python.values())
    # print(i)

# for key, value in python.items():
#     print(i)





# def get_extension(filename):
#     s = filename[:: -3]
#     n = filename[:: -4]
#     if s in ["png"]:
#         return "Расширение файла - png"
#     elif n in ["jpeg"]:
#         return "Расширение файла - jpeg"
#     elif n in ["html"]:
#         return "Расширение файла - html"
#     elif s in ["doc"]:
#         return "Расширение файла - doc"
#     elif n in ["xlsx"]:
#         return "Расширение файла - xlsx"
#     else:
#         None









# def buy_car(model: str, year: int, usage: int, color: str, owner: int, price: float, left_wheel: bool):
#     if (model.upper() in ["TOYOTA", "LEXUS"]
#     and (
#     (year >= 2004 and usage <= 150000 and color == "white" or color == "grey" and owner <= 2 and price <= 10000 and left_wheel == True) or
#     (year >= 2004 and usage <= 200000 and color == "white" or color == "grey" and owner <= 2 and price <= 8000 and left_wheel == True)
#         )
#     ):
#         return True
#     else:
#         return False
# result = buy_car("lexus", 2004, 150000, "grey", 1, 1000, True)
# print(result)

# Написать программу по выбору компьютера. 
# Нужен компьютер от 4 до 8 GB оперативной памяти.
# Размер жесткого диска как минимум 256, если SSD. Если HDD, то как минимум 1 терабайт.
# Стоимость ноутбука не должна превышать 1000$.
# Состояние новый.
# Вводные слова: 'ssd', 'hdd'
# def choose_pc(ram: int, hdd: int, hdd_type: str, price: float, condition: bool):
    


    # if (model in  ["TOYOTA", "LEXUS"]
    #     and (
    #     (year >= 2004 and usage <= 150000 and color == white or grey and  owner <= 2 and price <= 10000 and left_wheel == True) or 
    #     (usage >= 200000 and price <= 8000)
    #     ):
    #     return True
    # else:
    #     return False
    # if (district in ["чон-арык", "байтик", "ортосай"] 
    # and (
    #     (material == "кирпич" and area <= 4 and price <= 50000) or 
    #     (material == "пескоблок" and area <= 5 and  price <= 45000)
    #     )
    # ):
    #     return True
    # else:
    #     return False


    
# list comprehensions
# генераторы списков
# num_list = []
# for i in range(1, 1001):
#     num_list.append(i)
# print(nuist.append(i)
# print(num_list)
# num_list = [i ** 2 if i % 100 != 0 else "Null" for i in range(1, 1001) if i % 2 == 0]
# print(num_list)
# lists = ["apple", "banana", "cherry", "peach"]
# new_fruits = [fruit if fruit != "banana" else "potato" for fruit in lists ]

# numbers_id = [ord(i) for i in "python"]
# chars = [chr(i) for i in numbers_id]
# print("".join(chars))

from datetime import timedelta, datetime
lists = []
before = datetime.now()
number_list = [i for i in range(1, 10001)]

delta = datetime.now() - before
print(delta)




