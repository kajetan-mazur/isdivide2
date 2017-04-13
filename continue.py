

for i in range(100):
    if i % 35 != 0:
        print(i)

for i in range(100):
    if i % 35 == 0:
        continue
    else:
        print(i)


for i in range(1,101):
    if i % 3 ==0 and i % 5 ==0:
        print("FizzBuzz")
        continue
    if i % 3 == 0:
        print("Fizz")
        continue
    if i % 5 == 0:
        print("Buzz")
        continue
    print(i)