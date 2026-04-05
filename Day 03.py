# DAY 3: 30 Days of python programming

# 1-2-3
age = 31
height = 5.8
complex_number = 4-4j

#4
triangle_base = int(input("Enter the base: "))
triangle_height = int(input("Enter the height: "))
print('The area of the triangle is: ', 0.5 * triangle_base * triangle_height)

#5
side_a = int(input("Enter the side a: "))
side_b = int(input("Enter the side b: "))
side_c = int(input("Enter the side c: "))
print('The perimeter of the triangle is: ', side_a + side_b + side_c)\

#6
rectangle_width = int(input("Enter the width: "))
rectangle_height = int(input("Enter the height: "))
print('The area of the rectangle is: ', rectangle_width * rectangle_height)
print('The perimeter of the rectangle is: ', side_a + side_b + side_c)

#7
circle_radius = int(input("Enter the radius: "))
print('The area of the circle is: ', 3.14 * circle_radius * circle_radius)
print('The perimeter of the circle is: ', 2 * 3.14 * circle_radius)

#8
m = 2
b = -2
print('Slope: ', m)
print('x-intercept: ', -b / m)
print('y-intercept: ', b)

#9
x1, y1, x2, y2 = 2, 2, 6, 10
print('Euclidean Slope: ', (y2 - y1) / (x2 - x1))

#10
print(m == ((y2-y1)/(x2-x1)))

#11
print('y: ', ((-1^2) + (-1*6) + 9))

#12
len_python = len('python')
len_dragon = len('dragon')
print(len_python != len_dragon)

#13-14-15 - check if 'on' is found in both 'python' and 'dragon'
print('on' in ('python' and 'dragon'))
print('jargon' in 'I hope this course is not full of jargon')

#16
len_python_float = float(len_python)
len_python_string = str(len_python)
print(len_python_float, len_python_string)

#17 - Checking if number is even or odd
print( 6 % 2 == 0)
print( 5 % 2 == 0)

#18
print(7 // 3 == int(2.7))

#19
print(type('10') == type(10))

#20
print(int('9.8') == 10)

#21 - Job info
job_hours = int(input("Enter the hours: "))
job_rate_per_hour = int(input("Enter the rate per hour: "))
print('Your weekly earning is: ', (job_rate_per_hour * job_hours))

#22
years_lived = int(input('Enter number of years you have lived:'))
print('You have lived for', years_lived*365*24*60*60 , 'seconds')

#23
print(1, 1**0, 1**1, 1**2, 1**3)
print(2, 2**0, 2**1, 2**2, 2**3)
print(3, 3**0, 3**1, 3**2, 3**3)
print(4, 4**0, 4**1, 4**2, 4**3)
print(5, 5**0, 5**1, 5**2, 5**3)