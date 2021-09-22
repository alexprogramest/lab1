from sys import argv  # for using argv

functions = ['add', 'subtract', 'multiply', 'divide', 'power']
correct_input = False
input1, input2 = int(argv[2]), int(argv[3])


def operation():  # Checking which operator it is
    if argv[1] == functions[0]:
        print(input1 + input2)
    elif argv[1] == functions[1]:
        print(input1 - input2)
    elif argv[1] == functions[2]:
        print(input1 * input2)
    elif argv[1] == functions[3]:
        try:
            print(round(input1 / input2, 2))
        except ZeroDivisionError:
            print("Dividing by zero! Try again!")
    elif argv[1] == functions[4]:
        print(input1 ** input2)


if argv[2].isdigit() and argv[3].isdigit() and argv[2] in functions:  # Checking the numbers and output writing
    operation()
else:
    print("Wrong entry! Try again")
