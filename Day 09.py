# DAY 9: 30 Days of python programming

# Exercise Level 1

#1
user_age = int(input("Enter your age: "))
if user_age >= 18:
    print("You are old enough to drive!")
else:
    print("You need {} more years to learn to drive!".format(18 - user_age))

#2
cpu_age = int(input("Enter your age, cpu: "))
if cpu_age - user_age == 1:
    if cpu_age > user_age:
        print('You are 1 year older than me')
    else:
        print('You are 1 year younger than me')
elif cpu_age - user_age > 2:
    print('You are {} years older than me'.format(cpu_age - user_age))
else:
    print('You are same age as me')

#3
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
if a > b:
    print('{} is greater than {}'.format(a, b))
elif a < b:
    print('{} is less than {}'.format(a, b))
else:
    print('{} is equal to {}'.format(a, b))


# Exercise level 2

#1
user_marks = int(input("Enter your marks: "))
if user_marks > 90 and user_marks < 100:
    print("You marks are {} and grade is A".format(user_marks))
elif user_marks > 80:
    print("You marks are {} and grade is B".format(user_marks))
elif user_marks > 70:
    print("You marks are {} and grade is C".format(user_marks))
elif user_marks > 60:
    print("You marks are {} and grade is D".format(user_marks))
elif user_marks > 0:
    print("You marks are {} and grade is F".format(user_marks))
else:
    print("Enter the valid marks")

#2
month_name = input("Enter the name of the month: ")
if month_name == "December" or month_name == "January" or month_name == "February":
    print('The season is Winter')
elif month_name == "March" or month_name == "April" or month_name == "May":
    print('The season is Spring')
elif month_name == "June" or month_name == "July" or month_name == "August":
    print('The season is Summer')
else:
    print('The season is Autumn')

#3
fruits = ['banana', 'orange', 'mango', 'lemon']
user_fruit = input("Enter the name of the fruit: ")
if user_fruit not in fruits:
    print('The fruit is not in the list')
    fruits.append(user_fruit)
    print("The new list: ", fruits)
else:
    print('The fruit is in the list')


# Exercise Level 3

#1
person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

if 'skills' in person:                              #1
    middle = len(person['skills'])//2
    print(person['skills'][middle])


if 'skills' in person:
    if 'python' in person['skills']:
        print(person['skills']['python'])


if 'skills' in person:
    if 'React' and 'JavaScript' in person['skills']:
        print("He is a front end developer")
    elif 'Node' and 'Python' and 'MongoDB' in person['skills']:
        print("He is a back end developer")
    elif 'React' and 'Node' and 'MongoDB' in person['skills']:
        print('He is a full stack developer')
else:
    print('Unkown Title')


if person.get('is_married') == True and person.get('country') == 'Finland':
    print('{} {} lives in {}. He is married'.format(person['first_name'], person['last_name'], person['country']))