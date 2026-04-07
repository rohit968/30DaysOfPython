import random
import string

def generate_user_id():
    chars = string.ascii_letters + string.digits
    return ''.join(random.choices(chars, k=6))

def user_id_gen_by_user():
    num_of_chars = int(input("How many characters would you like? "))
    num_of_ids = int(input("How many ids would you like? "))
    chars = string.ascii_letters + string.digits
    user_ids = []
    for i in range(num_of_ids):
        user_ids.append(''.join(random.choices(chars, k=num_of_chars)))
    return user_ids

def rgb_color_gen():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return 'rgb({}, {}, {})'.format(r, g, b)

def list_of_hexa_colors():
    hex_chars = '0123456789abcdef'
    num_of_hexa = int(input("How many hexa colors would you like? "))
    colors = []
    for _ in range(num_of_hexa):
        color = '#' + ''.join(random.choice(hex_chars) for _ in range(6))
        colors.append(color)
    return colors

def list_of_rgb():
    num_of_rgb = int(input("How many rgb would you like? "))
    list_of_rgb_colors = []
    for i in range(num_of_rgb):
        list_of_rgb_colors.append(rgb_color_gen())
    return list_of_rgb_colors

def generate_colors():
    color_choice = input("Would you like hexa or rgb? ")
    if color_choice == 'hexa':
        return list_of_hexa_colors()
    elif color_choice == 'rgb':
        return list_of_rgb()
    else:
        return "Select either hexa or rgb"
