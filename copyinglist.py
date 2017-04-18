result = 3

list_a = ["zero", "one", result]
print("list a:", list_a)

result = 43
print("list a changed:", list_a)
print()

list_b = list_a.copy()
print("list b copied from a:", list_b)

print("Lets add element to list a")
list_a.append("new")
print(list_a)
print(list_b)

print(id(list_a))
print(id(list_b))