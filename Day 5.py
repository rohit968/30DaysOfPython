# DAY 5: 30 Days of python programming

#Exercise Level 1

#1 Declaring empty list
empty_list = []

#2
fruits = ["apple", "banana", "cherry", 'kiwi', 'mango']

#3
print(len(fruits))

#4 Print first, middle and last element
print(fruits[0], fruits[len(fruits)//2], fruits[-1])

#5 Personal Info
mixed_data_types = ['Rohit Tiwari', 31, 5.5, 'Married', 'Gwalior']

#6-25
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print(it_companies) #7
print(len(it_companies)) #8
print(it_companies[0], it_companies[len(it_companies)//2], it_companies[-1]) #9

it_companies[3] = 'Nvidia' #10
print(it_companies)

it_companies.append('Salesforce') #11 Add a company

it_companies.insert(3, 'Nothing') #12 Insert an item at a specific index

print(it_companies[0].upper()) #13

print((' # ').join(it_companies)) #14 Join the list

print('Nvidia' in it_companies) #15 Check if a company is in list

it_companies.sort() #16 Sorting the list

it_companies.reverse() #17 reversing the list

print(it_companies[:3]) #18

print(it_companies[-3:-1]) #19

print(it_companies[:len(it_companies)//2] + it_companies[len(it_companies)//2 + 1:]) #20 Slice the middle element or elements from the list

del it_companies[0]  #21 Delete the 1st item or a specific item in the list

del it_companies[len(it_companies)//2] #22

del it_companies[-1] #23

it_companies.clear() #24 Removing all the items in the list

del it_companies #25 Deleting the it_companies varialble

#26 - 27
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
front_end.extend(back_end)

full_stack = front_end #27
full_stack.insert(5, 'Python')
full_stack.insert(6, 'SQL')

