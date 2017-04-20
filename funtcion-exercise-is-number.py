def is_number_in_range(number,number_range):
    if number in number_range:
        return True
    else:
        return False

x = 23
y = range(1,23)
is_number_in_range(x,y)
print(is_number_in_range(x,y))