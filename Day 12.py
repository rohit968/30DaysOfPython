# DAY 12: 30 Days of python programming
import mymodule
from mymodule import *

# Exercise Level 1

#1
user_id = generate_user_id()
print(user_id)

#2
id_gen_by_user = user_id_gen_by_user()
for id in id_gen_by_user:
    print(id)

#3
rgb_by_user = rgb_color_gen()
print(rgb_by_user)

#Exercise Level 2

#1
hexa_colors = list_of_hexa_colors()
print(hexa_colors)

#2
rgb_colors = list_of_rgb()
print(rgb_colors)

#3
hexa_or_rgb = generate_colors()
print(hexa_or_rgb)


# Exercise Level 3

#1
shuffled_list_result = shuffle_list(['banana', 'apple', 'kiwi', 'mango', 'grape'])
print(shuffled_list_result)

#2
random_unique_num = seven_unique_random_num()
print(random_unique_num)