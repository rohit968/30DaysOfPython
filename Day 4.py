# DAY 4: 30 Days of python programming

#1-2 Concatenating the string
str1 = 'Thirty', 'Days', 'Of', 'Python'
str2 = 'Coding', 'For' , 'All'
print(' '.join(str1))
print(' '.join(str2))

#3-30

#3 Declaring and assigning a variable
company = "Coding For All"

#4 Printing the variable
print(company)

#5 Printing length of the variable
print(len(company))

#6 Making all the letter uppercase
print(company.upper())

#7 Making all the characters lowercase
print(company.lower())

#8 Capitalize(), Title(), SwapCase()
print(company.capitalize())
print(company.title())
print(company.swapcase())

#9 Slice
print(company[6:])

#10 Index, Find,
print(company.index('Coding'))
print(company.find('Coding'))

#11-12 Replace
print(company.replace('Coding', 'Python'))
print(('Python for everyone').replace('Python for everyone', 'Python for all'))

#13-14 Split
print(company.split(' '))
print(("Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon").split(','))

#15
print(company[0])

#16
print(company[-1])

#17
print(company[10])

#18-19
print("PFE")
print("CFL")

#20-21 index
print(company.index('C'))
print(company.index('F'))

#22
print(('Coding for all people').rfind('l'))

#23-24
print(('You cannot end a sentence with because because because is a conjunction').index('because'))
print(('You cannot end a sentence with because because because is a conjunction').rindex('because'))

#25
print(('You cannot end a sentence with because because because is a conjunction').replace("because because because", "").strip())

#26-27
print(('You cannot end a sentence with because because because is a conjunction').find('because'))

#28
print(company.startswith('Coding'))

#29
print(company.endswith('Coding'))

#30
print(('   Coding For All      ').strip())

#31
print(('30DaysOfPython').isidentifier())
print(('thirty_days_of_python').isidentifier())

#32
libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print(' # '.join(libraries))

#33 Line escape sequence
print('I am enjoying this challenge \nI just wonder what is next.')

#34 Tab sequence
print('Name\t\tAge\t\tCountry\t\tCity')
print('Asabeneh\t250\t\tFinland\t\tHelinski')

#35
radius = 10
area = 3.14 * radius ** 2
print('The area of a circle with radius {} is {} meters square'.format(radius, area))

#36
num_1 = 8
num_2 = 6
print(f'{num_1} + {num_2} = {num_1 + num_2}')
print(f'{num_1} - {num_2} = {num_1 - num_2}')
print(f'{num_1} * {num_2} = {num_1 * num_2}')
print(f'{num_1} / {num_2} = {num_1 / num_2}')
print(f'{num_1} % {num_2} = {num_1 / num_2}')
print(f'{num_1} // {num_2} = {num_1 / num_2}')
print(f'{num_1} ** {num_2} = {num_1 ** num_2}')
