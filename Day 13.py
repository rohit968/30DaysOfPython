# DAY 13: 30 Days of python programming

#Exercise

#1
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
positive_list = [i for i in numbers if i >= 0]
print(positive_list)

#2
list_of_lists =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flaten_list = [item for sub_item in list_of_lists for item in sub_item ]
print(flaten_list)

#3
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
new_list = [' '.join(item) for sub_item in names for item in sub_item]
print(new_list)
