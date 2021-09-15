def print_result(result, result_value):  # result printing
    print('result = (', result, ', ', result_value, ')')


print("Type the numbers with the operators")
main_str = input()
operators = ['+', '-', '*', '/']
possible_sign = True
operators_str = []

for i in range(len(main_str)):  # Checking which operator it is
    if main_str[i] == operators[0]:
        operators_str.append(operators[0])
    elif main_str[i] == operators[1]:
        operators_str.append(operators[1])
    elif main_str[i] == operators[2]:
        operators_str.append(operators[2])
    elif main_str[i] == operators[3]:
        operators_str.append(operators[3])
    else:
        operators_str.append('\0')

if main_str[0].isdigit():  # Checking: is the string correct? (If no - exit program)
    for i in range(1, len(main_str)):
        if main_str[i].isdigit():
            possible_sign = True
        elif operators_str[i] == main_str[i]:
            if not possible_sign:
                exit()
            possible_sign = False
        else:
            exit()
else:
    exit()

numbers = []
index_num = 0
start, end = 0, 0
for i in range(1, len(main_str)):
    if operators_str[i] == main_str[i]:
        end = i
        numbers.append(int(''.join(main_str[start:end])))
        start, end = i + 1, i + 1
numbers.append(int(''.join(main_str[start:len(main_str)])))
# counting
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
print_result(True, round(final_result, 3))
