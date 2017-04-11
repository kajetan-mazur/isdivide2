number = input("give number: ")
divided = input("divided by: ")

if number.isdigit() and divided.isdigit():
    if int(number) % int(divided) == 0:
        print("Number is divided by ", divided)
        print("Result: ", int(number) / int(divided))
    else:
        print("Number is not divided by ", divided)
        print("Result: ", int(number) / int(divided))
else:
    print("Give number!!")
