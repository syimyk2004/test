
# x = "hello world! I beutiful"

# print(x.lower())
# print('Old text: ' + x)
# upper_cased = x.upper()
# lower_cased = x.lower()
# print(upper_cased.isupper())
# print(lower_cased.islower())
# print(x.isupper())
# print(x.islower())

# print('xxx777'.isalnum())
# print('xxx777!'.isalnum())
# print('xxx777'.isalpha())
# print('xxx'.isalpha())
# print('   '.isspace())
# print(''.isspace())
# empty_string = ''
# print(empty_string == '') #true
# print(empty_string == ' ')  #false
# print(empty_string.strip(' ') == '') #true
# empty_string = ' '
# print(empty_string.strip() == '')

# empty_string = '' 
# if not empty_string:
# 	print('not empty')
# else:
# 	print('empty')

# x = str('hello')
# print(x.startswith('he'))
# print(x.endswith('lo'))
# split = x.split('l')
# print(type(split))
# print(split)
# split = x.split('e')
# print(split)
# some_data = '4;8;15;16;23;42'
# separated_data = some_data.split(';')
# print(separated_data)

def get_extension(filename):
    if filename == '.png, jpeg, html, doc, xlsx':
        return (f"Расширение файла - {filename}")
    else:
        return None
result = get_extension(".png, jpeg, html, doc, xlsx")
print(result)


# print(separated_data[3])


# def func(district: str, material: str, area: float, price):
#     if (district in ["чон-арык", "байтик", "ортосай"] 
#     and (
#         (material == "кирпич" and area <= 4 and price <= 50000) or 
#         (material == "пескоблок" and area <= 5 and  price <= 45000)
#         )
#     ):
#         return True
#     else:
#         return False

# result = func("байтик", "кирпич", 5, 50000)
# print(result)

