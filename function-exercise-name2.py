name = "john"

def print_names(name_2):
    name = "anna"
    name = name.capitalize()
    name_2 = str(name_2).capitalize()

    print(name,name_2)

print_names("joanna")
print(name)

name1="john"

def print_names1(name_2):
    global name1
    name1 = "anna"
    name1 = name1.capitalize()
    name_2 = str(name_2).capitalize()

    print(name1,name_2)

print_names1("joanna")
print(name1)