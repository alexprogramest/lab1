# argv[0] - 'Exercise1.py' !!!!!!!
from sys import argv  # for using argv

operators = ['+', '-', '*', '/']
correct_input = False
input1, input2 = int(argv[1]), int(argv[3])


def operation():  # just checking which operator it is
    if argv[2] == operators[0]:
        print(input1 + input2)
    elif argv[2] == operators[1]:
        print(input1 - input2)
    elif argv[2] == operators[2]:
        print(input1 * input2)
    elif argv[2] == operators[3]:
        print(round(input1 / input2, 2))


for i in range(4):  # looking for the operator
    if argv[2] == operators[i]:
        correct_input = True

if argv[1].isdigit() and argv[3].isdigit() and correct_input:  # Finally, checking the numbers and output writing
    operation()
else:
    print("Wrong entry! Try again!")
