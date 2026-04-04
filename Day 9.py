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


