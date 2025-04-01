import string

def turn_digit_to_letter(post_code):
    alphabet = list(string.ascii_lowercase)
    post_code = str(post_code)
    first_name = ''
   
    for i in range(0, len(post_code), 2):
        pair = int(post_code[i: i+2])
        index = pair % len(alphabet)
        first_name += alphabet[index]

    return first_name