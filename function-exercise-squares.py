def square(number):
    return number**2


def rectangular_field(a,b):
    if a == b:
        return square(a)
    else:
        return a*b

print(rectangular_field(2,2))
print(rectangular_field(2,5))