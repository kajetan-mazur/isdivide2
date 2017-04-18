#remove duplicates from list
list_numbers = [10,20,30,40,20,45,54,45,90,90,101]
list_without_duplicates=[]

for element in list_numbers:
    if element not in list_without_duplicates:
       list_without_duplicates.append(element)

print(list_without_duplicates)