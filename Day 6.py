c

# Exercise Level 1

# 1
empty_tuple = ()

#2
brothers = ('Aditya', 'Rohit', 'Saurabh', 'Nikhil')
sisters = ('Shikhs', 'Deepa', 'Shreya')

#3
siblings = brothers + sisters

#4
print(len(siblings))

#5
family_members = siblings + ('Raj', 'Rekha')


# Exercise Level 2

#1
family, *siblings = family_members[-2:], family_members[:7]

#2
fruits = ('bananna', 'apple', 'kiwi')
vegetables = ('ladyfinger', 'tomato', 'potato')
animal_products = ('urea', 'fodder')
food_stuff_up = fruits + animal_products + vegetables

#3
food_stuff_lt = list(food_stuff_up)

#4
print(food_stuff_lt[len(food_stuff_lt)//2])

#5
print('First three items: ', food_stuff_lt[:3])
print('Last three items: ', food_stuff_lt[-3:])

#6
del food_stuff_up

#7
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)