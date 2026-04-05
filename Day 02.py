# DAY 2: 30 Days of python programming

#Declaring variable
first_name = "Rohit"
last_name = "Tiwari"
full_name = "Rohit Tiwari"
country = "India"
city = "Gwalior"
age = 31
year = 2026
is_married = True
is_true = True
is_light_on = False
address, contact, has_vehicle = "Gwalior", 1234567890, False

#Checking data type
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(age))
print(type(country))
print(type(city))
print(type(is_married))
print(type(is_light_on))
print(type(is_true))
print(type(is_light_on))

#Finding the lenght
print(len(first_name))

# Arithmatic Operations
num_one = 5
num_two = 4
total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_one % num_two
exp = num_one ** num_two


#Circle
radius = 30
area_of_circle = 3.14 * (radius ** 2)
circum_of_circle = 2 * 3.14 * radius
print(radius, area_of_circle, circum_of_circle)

user_radius = int(input("Enter radius: "))
print('user_area:', 3.14 * (user_radius ** 2))

#User info
user_first_name = input("Enter your first name: ")
user_last_name = input("Enter your last name: ")
user_country = input("Enter your country: ")
user_age = input("Enter your age: ")
print(user_first_name, user_last_name, user_country, user_age)
