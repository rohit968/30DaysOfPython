# DAY 7: 30 Days of python programming

# Exercises: Level 1

#1 - 5
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}

print(len(it_companies)) #2 length of set

it_companies.add('Twitter') #3 add an item to the set

it_companies.update(['Github', 'Salesforce']) #4 add multiple item to the set

it_companies.remove('Github') #5 remove an item from the set


#6 Remove and discard both are used to delete an item from the set. If an item is not present is the set, remove() will raise errors but discard() will not.


#Exercise Level 2

# 1 - 7
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

print(A.union(B)) #1 joining A and B

print(A.intersection(B)) #2 intersection between A and B

print(A.issubset(B))  #3 check if A is subset of B

print(A.isdisjoint(B)) #4 check if disjoint

print(A.union(B), B.union(A)) #5 A join B and B join A

print(A.symmetric_difference(B)) #6 checking symmetric difference

del A
del B #7 completely deleting the sets


#Exercise Level 3

age = [22, 19, 24, 25, 26, 24, 25, 24]

#1
age_set = set(age) # converting list to set
print('Length of set', len(age_set))
print('Length of list', len(age))

#2 String -> collection of characters, List -> ordered collection of multiple datatypes, Tuples -> Ordered and unchangable collection, Sets -> unordered and un-indexed collection of items

#3
prac_str = "I am a teacher and I love to inspire and teach people"
result = (prac_str.split(' '))
print(len(set(result)))