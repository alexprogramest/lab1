main_str = input("Type the numbers with the operators\n")
operators = ['+', '-', '*', '/']
operators_str = []


def print_result(result, result_value):  # result printing
    print('result = (' + str(result) + ', ' + str(result_value) + ')')


def operator_check():
    for j in range(len(main_str)):  # Checking which operator are in string
        if main_str[j] == operators[0]:
            operators_str.append(operators[0])
        elif main_str[j] == operators[1]:
            operators_str.append(operators[1])
        elif main_str[j] == operators[2]:
            operators_str.append(operators[2])
        elif main_str[j] == operators[3]:
            operators_str.append(operators[3])
        else:
            operators_str.append('\0')


def string_check(possible_sign):
    if main_str[0].isdigit():  # Checking: is the string correct? (If no - exit program)
        for j in range(1, len(main_str)):
            if main_str[j].isdigit():
                possible_sign = True
            elif main_str[j] in operators:
                if not possible_sign:
                    print_result(False, None)
                    exit()
                if j == len(main_str) - 1:
                    print_result(False, None)
                    exit()
                possible_sign = False
            else:
                print_result(False, None)
                exit()
    else:
        print_result(False, None)
        exit()


def counting(numbers):
    counter = 0
    final_result = numbers[counter]
    for i in range(1, len(main_str)):
        if operators_str[i] == main_str[i]:
            if main_str[i] == operators[0]:
                counter += 1
                final_result += numbers[counter]
            elif main_str[i] == operators[1]:
                counter += 1
                final_result -= numbers[counter]
            elif main_str[i] == operators[2]:
                counter += 1
                final_result *= numbers[counter]
            elif main_str[i] == operators[3]:
                counter += 1
                final_result /= numbers[counter]
    return final_result


def number_list(numbers):  # getting the list of all numbers
    start, end = 0, 0
    for i in range(1, len(main_str)):
        if operators_str[i] == main_str[i]:
            end = i
            numbers.append(int(''.join(main_str[start:end])))
            start, end = i + 1, i + 1
    numbers.append(int(''.join(main_str[start:len(main_str)])))
    return numbers


string_check(True)
operator_check()

# counting and printing the final result
print_result(True, round(counting(number_list([])), 3))
