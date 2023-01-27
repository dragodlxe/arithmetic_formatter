def arithmetic_arranger(problems: list, ans=False):
    
    if len(problems) > 5:
        return 'Error: Too many problems.'

    problems_result = ''
    operator = [i.split()[1] for i in problems]
    
    operation = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b
    }

    for i in operator:
        if i != '+' and i != '-':
            return "Error: Operator must be '+' or '-'."

    number_1 = [i.split()[0] for i in problems]
    number_2 = [i.split()[2] for i in problems]
    longest_number = []
    
    for x, y in zip(number_1, number_2):
        if not(x.isdigit()) or not(y.isdigit()):
            return 'Error: Numbers must only contain digits.'
        elif len(x) > 4 or len(y) > 4:
            return 'Error: Numbers cannot be more than four digits.'
        else:
            temp = len(x) if int(x) > int(y) else len(y)
            longest_number.append(temp)

    for num1, length in zip(number_1, longest_number):
        problems_result += '  '+(' ' * (length - len(num1))) + num1 + '    '

    problems_result = problems_result.rstrip()
    problems_result += '\n'

    for op, num2, length in zip(operator, number_2, longest_number):
        problems_result += op + ' ' + (' ' * (length - len(num2))) + num2 + '    '

    problems_result = problems_result.rstrip()
    problems_result += '\n'

    for i in range(len(problems)):
        problems_result += ('-' * (longest_number[i]+2)) + '    '

    problems_result = problems_result.rstrip()
    
    if ans:
        problems_result += '\n'

        for num1, op, num2, length in zip(number_1, operator, number_2, longest_number):
            temp = operation[op](int(num1), int(num2))
            problems_result += ' ' * (length+2-len(str(temp))) + str(temp) + '    '
            

    problems_result = problems_result.rstrip()
    return problems_result


def main():
    print(arithmetic_arranger(["32 - 698", "3801 - 2", "45 + 43", "123 + 49"], True))


if __name__ == "__main__":
    main()
