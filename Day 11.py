# DAY 11: 30 Days of python programming

# Exercise Level 1

#1
def add_two_numbers(num1, num2):
    return num1 + num2
print(add_two_numbers(3,4))

#2
def area_of_circle(radius):
    return 3.14 * radius * radius
print(area_of_circle(5))

#3

def add_all_numbers(*args):
    sum = 0
    for arg in args:
        if type(arg) == int:
            sum += arg
        else:
            print("Give me numbers only")
    print(sum)
add_all_numbers(1,2,3,4,5,6,7,8,9,10)

#4
def convert_celsius_to_fahrenheit(temp):
    return temp * 9 / 5 + 32
print(convert_celsius_to_fahrenheit(1))

#5
def check_season(month_name):
    if month_name == "December" or month_name == "January" or month_name == "February":
        print('The season is Winter')
    elif month_name == "March" or month_name == "April" or month_name == "May":
        print('The season is Spring')
    elif month_name == "June" or month_name == "July" or month_name == "August":
        print('The season is Summer')
    else:
        print('The season is Autumn')

check_season("February")

#6
def print_list(*args):
    for arg in args:
        print(arg)
print_list('Rohit', 'Tiwari', 'Aditya', 'Tiwari')

#7
def reverse_list(lst):
    reversed_list = []
    for item in lst:
        reversed_list.insert(0, item)
    print(reversed_list)
reverse_list(["A", "B", "C"])

#8
def capitalize_list_items(lst):
    for item in lst:
        print(item.capitalize())
capitalize_list_items(["a", "b", "c"])

#9
def add_item(lst, item):
    lst.append(item)
    return lst
print(add_item(['Potato', 'Tomato', 'Mango', 'Milk'], 'Kiwi'))

#10
def remove_item(lst, item):
    lst.remove(item)
    return lst
print(remove_item(['Potato', 'Tomato', 'Mango', 'Milk'], 'Mango'))

#11
def sum_of_numbers(num):
    sum = 0
    for n in range(num):
        sum += n
    return sum
print(sum_of_numbers(5))

#12
def sum_of_odds(num):
    sum = 0
    for n in range(num):
        if n % 2 != 0:
            sum += n
    return sum
print(sum_of_odds(5))

#13
def sum_of_evens(num):
    sum = 0
    for n in range(num):
        if n % 2 == 0:
            sum += n
    return sum
print(sum_of_evens(5))