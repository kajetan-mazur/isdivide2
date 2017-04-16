#Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included)
for x in range(1500,2701):
    if (x % 7 == 0) and (x % 5 == 0):
        print(x)

#Write a Python program to convert temperatures to and from celsius, fahrenheit.
celcius = input('Put temperature in celcius: ')
print('Fahrenheit: ',int(celcius) * 9/5 +32)

fahrenheit = input('Put temprature in fahenheit: ')
print('Celcius: ', (int(fahrenheit)-32)*5/9)

temprature = input('Put temprature (e.g., 80f or 32c): ')
number = int(temprature[:-1])
scale = temprature[-1]

if scale == 'c':
    result = int(number*9/5 + 32)
    other_scale = 'fahrenheit'
elif scale == 'f':
    result = int((number-32)*5/9)
    other_scale = 'celcius'
else:
    print('Input proper convention')
    quit()
print('temprature in ',other_scale,'is',result,'degrees')













