number = input("give number: ")
divided = input("divided by: ")

if number.isdigit() and divided.isdigit():
    result = int(number)/int(divided)
    if round(result, 2).is_integer():
        print('Number {} is divided by {}'.format(number, divided))
    else:
        print('Number {} is not divided by {}'.format(number, divided))
        print('Result: {:.2f}', result)
else:
    print("Give number!!")
