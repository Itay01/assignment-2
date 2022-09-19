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
print("\n")

# Assignment 5
students_five_units = 0
for student in range(1, 976):
    print(f"\nHello student number {student}!")
    name = input("Enter your name: ").title()
    while True:
        try:
            units = int(input("Enter the number of units you are learning: "))
            grade = int(input("Enter your grade in this class: "))
        except ValueError:
            print("The grade and units must be an integer!\n")
        else:
            if 3 <= units <= 5 and 0 <= grade <= 100:
                if units == 5:
                    students_five_units += 1
                break
            else:
                print("The numbers you entered are invalid!\n")

    print(f"The name of the student is {name}, he is in {units} units, and his grade in this class is {grade}.")
    if grade > 95:
        print("He got an A!")

print(f"\nThe number of students in 5 units is {students_five_units}!")
