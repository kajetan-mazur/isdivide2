list1 = ['three', 'four']
list2 = [2,3,4,5,67,3,3]
print(type(list1))

list3 = list('123566')
print(list3)

list4 = [1, "two", "three", 4]

for element in list4:
    print(element)
list_z = [[1,2,3],[4,5,6],[7,8,9]]

for element in list_z:
    for subelement in element:
        print(subelement)
print(list_z[1:3])
print(list_z.reverse())

list4b =[]
list4b.append(1)
print(list4b)