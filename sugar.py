list_numbers = [1,2,3,4,5,6,7,8,9]
list_numbers_squares = []

for element in list_numbers:
    list_numbers_squares.append(element*element)
print(list_numbers_squares)

list3 = [element**2 for element in list_numbers]
print(list3)

list4 = [element**2 for element in list_numbers if element%3 == 0]
print(list4)