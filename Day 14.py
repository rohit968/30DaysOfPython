# DAY 14: 30 Days of python programming

# Exercise Level 1

#1 Difference b/w map, filter and reduce
# map → transforms, filter → selects, reduce → aggregates (combines into one result).

#2 Difference b/w higher order function, closure and decorator.
# Higher-order function → takes/returns functions, closure → remembers outer variables, decorator → wraps & modifies a function’s behavior.

#3
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
for country in countries:
    print(country)

#4
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
for name in names:
    print(name)

#5
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for number in numbers:
    print(number)


# Exercise Level 2

#1
def capitals(country):
    return country.upper()
capital_country_name = map(capitals, countries)
print(list(capital_country_name))

#2
def square(num):
    return num ** 2
numbers_square = map(square, numbers)
print(list(numbers_square))

#3
def capital_name(name):
    return name.upper()
capital_name = map(capital_name, names)
print(list(capital_name))


