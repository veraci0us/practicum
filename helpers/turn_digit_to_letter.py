import string
import math

def turn_digit_to_letter(post_code):
    alphabet = list(string.ascii_lowercase)
    pairs = []
    first_name = ''
   
    for i in range(0, len(str(post_code)), 2):
        pairs.append(str(post_code)[i:i+2])

    for i in range(0, len(pairs)):
        digit = int(pairs[i])
        letters_num = len(alphabet)
        if digit < letters_num:
            first_name += alphabet[digit]
        else: 
            circle = math.floor(digit / letters_num)
            index = digit - (circle * letters_num)
            first_name += alphabet[index]

    return first_name