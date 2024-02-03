#Days 52, 53 - lambda functions, map,reduce,filter functions
from functools import reduce

def is_numeric(s):
    try:
        s = float(s)
        return True
    except:
        return False

def convert_str_to_num(s):
    try:
        s = int(s) if "." not in s else float(s)
    except:
        s = s
    return s

n = int(input("Enter number of elements in list: "))
user_list = []
for i in range(n):
    val = input("Enter an element: ")
    user_list.append(val)

user_list = list(map(convert_str_to_num, user_list))

numbers = list(filter(is_numeric, user_list))

non_numeric = [element for element in user_list if element not in numbers]

product = reduce(lambda x,y : x*y, numbers, 1)

print(f'''Original list - {user_list}
Numeric list - {numbers}
Non-numeric list - {non_numeric}
Product of numbers in numeric list - {product}''')