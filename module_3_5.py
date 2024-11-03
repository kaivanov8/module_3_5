        # Рекурсия module_3_5

def get_multipled_digits (number):
    str_number = str (number)
    first = int (str_number)//(10**(len(str_number)-1))
    if len(str_number) > 1 :
        return first*get_multipled_digits(int(str_number[1:]))
    else:
        return first

print(get_multipled_digits(40203))
