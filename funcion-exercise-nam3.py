def add_name(name,names=None):
    if names is None:
        names = []
    names.append(name)
    return names

name_list = add_name("Anna")
print(name_list)

name_list2 = add_name("John")
print(name_list2)

name_list3 = add_name("Karen")
print(name_list3)