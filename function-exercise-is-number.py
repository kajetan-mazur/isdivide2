def is_number_in_range(number,number_range):
    if number in number_range:
        return True
    else:
        return False

x = 23
y = range(1,23)
is_number_in_range(x,y)
print(is_number_in_range(x,y))

numbers = [23,45,67,89,232,345,4564]

for num in numbers:
    print(is_number_in_range(num,range(100)))