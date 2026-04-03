# DAY 8: 30 Days of python programming

#1 - creating an empty dictionary
dog = {}

#2
dog['name'] = 'Rocky'
dog['color'] = 'Brown'
dog['legs'] = 4
dog['age'] = 2

#3
student_dict = {'first_name':'Rohit', 'last_name':'Tiwari', 'gender':'Male', 'Age': 31, 'Marital Status':'Married', 'skills':['Python Developer', 'Web developer'], 'country':'India', 'city':'Delhi', 'address':'Delhi'}

#4
print(len(student_dict))

#5
skills = student_dict['skills']
print(type(skills))

#6
student_dict['skills'] = ['Python Developer', 'Web developer', 'Swift developer']

#7
dict_keys_list = student_dict.keys()
print(type(dict_keys_list))

#8
dict_values_list = student_dict.values()
print(type(dict_values_list))

#9
dict_items = student_dict.items()
print(dict_items)

#10
print(student_dict.pop('skills'))

#11
del student_dict
