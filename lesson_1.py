
# print('hello   world')

#  str1 = "nazgul" 
# print(len(str1))
# print(len(str1.strip()))
# print(dir(str1)) 





# txt = "hello bootcamp"
# make_new_txt = txt.maketrans('bootca', 'eeeeee')
# print(txt)
# print(txt.translate(make_new_txt))

# str_city = "new York city"
# town = str_city.replace('city', 'town')
# print(town)

# str1 =  "new York city"
# print(ord('Y'))
# print(ord('d'))
# rep_city = {
#     89: 68 
# }
# print(str1.translate(rep_city))

# sity = "new york city"
# # print(email.endswith("@gmail.ru"))
# # print(email.startswith("new"))
# # print(dir("w"))

# print(sity.find("k"))
# print(sity.rfind("k", 8, 11))



# num = 5 % 3
# num2 = 5 // 3
# print(num, num2)

# num = 5

# num += 5
# print(num)
# num = num + 5
# print(num)



# Назгуль Табылдиева, [14.10.2022 10:25]
# 4 - задача
# Должен
# знать либо python, либо java, либо javascript. Возраст от 18 до 65. Опыт
# от 3х лет. Зарплата до 60000. Вывести результат, подходит кандидат или
# нет.

# Язык программирования:
# Возраст:
# # Опыт:
# # Желаемая зарплата:
# from tkinter.tix import InputOnly


# leng = input("введите язык програмирования который вы знаете: ")
# age = int(input("введит ваш возраст: "))
# experience = int(input("Введите ваш опыт: "))
# sal = int(input("Введите желаемую зарплату: "))
# lengs = (leng == "python" or leng == "java"  or leng == "javascript")
# # print(lengs)
# ages = (age > 18 and age < 65)
# # print(ages)
# exe = (experience > 3) and (sal < 60000)
# # print(exe)
# sals = (sal < 60000)
# print(sals and lengs and ages and exe)

# def get_power(U, I):
#     return U * I


# num = 10
# if num == 10:
#     num = num / 2
#     if num == 5:
#         print(num / 2)


# from difflib import restore
# from unittest import result


# my_list = [1, 2,  3, 4]
# # if 2 in my_list:
# #     print("")
# # my_list.clear()
# my_list.reverse()
# print(my_list)
# # my_list.sort(reverse=True)

def palindrom(str_value):
    if str_value == str_value[:: -1]:
        return "this is polindrom!!!"
    else:
        return "No"
result = palindrom("sdlaf")
print(result)



# print(sum(my_list))
# if my_list:
#     result = sum(my_list) / len(my_list)
# print(round(result))


# my_list = [1, 3, 4]
# my_list.remove(1)



# lists = [1, 3, 5, "nazgul"]
# # for i in lists:
# #     print(i)


# for i in "Hello world":
#     print(i)



# znak = "ab35ed"
# numbers = []
# alfa = []
# for i in znak:
#     print(i)
#     if i.isdigit():
#         numbers.append(i)
#     elif i.isalpha():
#         alfa.append(i)
# print(numbers)
# print(alfa)


# num = [1, 3, 5, 20, 33, 36, 9, 10, 12, 30]
# g = []
# for i in num:
#     if i % 3 == 0 and i % 2 == 0:
#         g.append(i)
# print(g)



# num = []

# for i in list(range(1, 1000)):
#     if i % 2 == 0:
#         num.append(i)

# print(num)
    

# for i in range(4):
#     print("*****")




# num = int(input("ведите число: "))

# for i in range(1, 11):
#     print(f" {i} * {num} = {i * num}")



# def check_digit(a):
#     if a < 10:
#         return "Меньше 10"
#     elif a >= 10 and a < 100:
#         return "Число в промежутке между 10 и 100"
#     else:
#         return "Число больше 100"

# coutner = 0

# for i in range(1, 21):
#     coutner += i 
# else:
#     print("result", coutner)


# for i in range(1, 10):
#     if i % 2 == 0:
#         continue
# else:
#     print("end")

# list1 = []
# for i in range(1, 100): 
#     if i % 3 != 0:
#         continue
#     list1.append(i)
# else:
#     print(list1)





# # while
# i = 2
# while i <= 100:
#     print(i)
#     i += 1


# i = 0
# while i <= 100:
#     if i == 50:
#         break
#     print(i)
#     i += 1

# while True:
#     num1 = int(input("num1:"))
#     num2 = int(input("num2: "))
#     operation = input("operation: ")

#     if operation == "*":
#         print(num1 * num2)
#     elif operation 

# list1 = ["ilshat", "promak012"]
# attempts = 3
# while True:
#     if attempts == 0:
#        list1.clear()
#        print("Вы не зареганы")
#        break
#     login = input("Введите своё имя: ")
#     password = input("Введите свой пароль: ")
#     if login == list1[0] and password == list1[1]:
#         print("добро пожаловать!")
#         break
#     elif attempts > 0:
#         print("неверно")
#         attempts -= 1
    


# list() ; []
# tuple ()
# set() ; {}
# dict() ; {}
# tuple()
# tuples = ("nazgul", [1, 3, 4], 5)
# print(type(tuples))
# print(tuples)





# tuples = (1, 2, 4)
# tuples = list(tuples)
# tuples.append("nazgul")
# tuples = tuple(tuples)
# print(tuples)
# for i in tuples:
#     print(i)

# a = 4
# b = 9
# a, b = b, a
# print(a,b)
# tuples = ([1, 3, 4], 1, 4)
# lists, number, number2 = tuples
# print(id(lists))
# print(id(number))
# print(id(number2))


# tuples = ((), (), ('',), ('a', 'b'), 5, "asv" ('a', 'b', 'c'), ('d'))

# tuples = list(tuples)
# tupless = list()
# print(type(()) == tuple)
# for i in range(0, len(tuples)):
#     if type(i) == tuple and len() == 0:
#         continue
#     tupless.append(i)
# tuples = tuple(tupless)

# print(tupless)




# tuples = ((), ("a", "b"), "B", 5, (5, 8, ()))
# tuple_parity = ()
# tuple_parity = list(tuple_parity)
# if tuples % 2 == 0:
#     tuple_parity.append()
# print(tuple_parity)









