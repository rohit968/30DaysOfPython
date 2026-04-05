# DAY 10: 30 Days of python programming

#Exercise Level 1

#1
for i in range(10):
    print(i)

a = 0
while a < 10:
    print(a)
    a += 1

#2
for i in range(10, 0, -1):
    print(i)

a = 10
while a > 0:
    print(a)
    a -= 1

#3
for i in range(1, 8):
    print('#' * i)

#4
for i in range(1, 8):
    for j in range(1, 8):
        print('#', end=' ')
    print('\n')

#5
i = 0
while i < 11:
    print('{} * {} = {}'.format(i, i, i * i))
    i += 1

#6
tech_list = ['Python', 'Numpy','Pandas','Django', 'Flask']
for item in tech_list:
    print(item)

#7
for i in range (101):
    if i % 2 == 0:
        print(i)

#8
for i in range (101):
    if i % 2 != 0:
        print(i)


# Exercise Level 2

#1
sum_numbers = 0
for i in range(101):
    sum_numbers += i
print(sum_numbers)

#2
sum_odd, sum_even = 0, 0
for i in range(101):
    if i % 2 == 0:
        sum_even =  sum_even + i
    else:
        sum_odd = sum_odd + i
print('The sum of all evens are:, ', sum_even)
print('The sum of all odds are:, ', sum_odd)


# Exercise Level 3

#1
fruits = ['banana', 'orange', 'mango', 'lemon']
fruit_reverse = []
for fruit in fruits:
    fruit_reverse.insert(0, fruit)
print(fruit_reverse)

