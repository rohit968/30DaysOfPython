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

