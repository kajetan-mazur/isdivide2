numbers = range(9)

even_numbers = 0
odd_numbers = 0

for i in zakres:
    if i % 2 ==0:
        even_numbers +=1
    else:
        odd_numbers +=1




print("How many even numbers: {}, odd numbers {}".format(even_numbers,odd_numbers))