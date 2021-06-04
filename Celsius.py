# num_in_celsius = int(input('Enter a number in Celsius: '))

# num_converted = (F = (num_in_celsius * 9/5) + 32)

# print (num_converted)

try:
    C = int(input('Temp in C?'))
    F = (C * 9/5) + 32
    print(str(F) + " F")

except ValueError:
    print('not a number')