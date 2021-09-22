# argv[0] - 'Exercise1.py' !!!!!!!
from sys import argv  # for using argv

operators = ['+', '-', '*', '/']
input1, input2 = int(argv[1]), int(argv[3])


def operation():  # just checking which operator it is
    if argv[2] == operators[0]:
        print(input1 + input2)
    elif argv[2] == operators[1]:
        print(input1 - input2)
    elif argv[2] == operators[2]:
        print(input1 * input2)
    elif argv[2] == operators[3]:
        try:
            print(round(input1 / input2, 2))
        except ZeroDivisionError:
            print("Dividing by zero! Try again!")


if argv[1].isdigit() and argv[3].isdigit() and argv[2] in operators:  # Finally, checking the numbers and output writing
    operation()
else:
    print("Wrong entry! Try again!")
