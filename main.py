# Number verification
def number_verification():
    """Return integer number that is between 2-9."""
    while True:
        try:
            number_func = int(input(f"\nEnter a number that is between 2-9: "))
        except ValueError:
            print("The number must be an integer!\n")
        else:
            if 2 <= number_func <= 9:
                print("The number you entered is valid!\n")
                return number_func
            else:
                print("The number you entered is invalid!\n")


# Number for the assignments
number = number_verification()

# Assignment number 1
for i in range(1, number + 1):
    line = ''
    for num in range(1, i + 1):
        line += str(num)
    print(line)

for i in range(number, 1, -1):
    line = ''
    for num in range(1, i):
        line += str(num)
    print(line)
print("\n")

# Assignment number 2
for i in range(number, 1, -1):
    line = ''
    for num in range(1, i + 1):
        line += str(num)
    print(line)

for i in range(1, number + 1):
    line = ''
    for num in range(1, i + 1):
        line += str(num)
    print(line)
print("\n")

# Assignment number 3
for i in range(0, number):
    line = '' + ' ' * i
    for num in range(i + 1, number + 1):
        line += str(num)
    print(line)

for i in range(number - 2, -1, -1):
    line = '' + ' ' * i
    for num in range(i + 1, number + 1):
        line += str(num)
    print(line)
print("\n")

# Assignment number 4
for i in range(0, number - number // 2):
    line = '' + ' ' * i
    for num in range(i + 1, number + 1 - i):
        line += str(num)
    print(line)

if number == 2:
    print(" 1")
elif number % 2 == 0:
    print(' ' * (number // 2 - 1) + str(number // 2))


for i in range(number // 2 - 1, - 1, -1):
    line = '' + ' ' * i
    for num in range(i + 1, number + 1 - i):
        line += str(num)
    print(line)
