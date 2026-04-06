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


# Exercise Level 2

#1
def evens_and_odds(num):
    if num > 0:
        odds = 0
        evens = 0
        for n in range(num+1):
            if n % 2 == 0:
                evens += 1
            else:
                odds += 1
        return odds, evens

odds, evens = evens_and_odds(100)
print('The number of odds are, ', odds)
print('The number of evens are, ', evens)

#2
def factorial(num):
    if num == 1:
        return 1
    else:
        return num * factorial(num-1)
print(factorial(5))

#3
def is_empty(param):
    if not param:
        return 'Empty'
    else:
        return 'Not Empty'
print(is_empty(''))

#4
def greet(name = "guest"):
    print("Hello, " + name + "!")
greet()

#5
def show_args(**args ):
    for k, v in args.items():
        print('key', k, 'value', v)
show_args(name="Alice", age=30, city="New York")


# Exercise Level 3

#1
def is_prime(num):
    if num < 2:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2, num):
            if num % i == 0:
                return "Not a prime number"
            else:
                return "Prime Number"
print(is_prime(5))

#2
def is_unique(lst):
    if len(lst) == len(set(lst)):
        return "Unique items in list"
    else:
        return "Not Unique"
print(is_unique(["a", "b", "c"]))

#3
def is_unique(lst):
    return len({type(item) for item in lst}) == 1
print(is_unique(["a", "b", "c"]))

#4
