def arithmetic_arranger(problems, ans=False):
    
    if len(problems) > 5:
        return 'Error: Too many problems.'

    problems_result = ''
    operator = [i.split()[1] for i in problems]
    
    operation = {
        '+': lambda x, y : x + y, 
        '-': lambda x, y : x - y 
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
            temp = len(x) if x >= y else len(y)
            longest_number.append(temp)

    return f'{longest_number=}'


def main():
    print(arithmetic_arranger(["32 - 698", "3801 - 2", "45 + 43", "123 + 49"]))
    
if __name__ == "__main__":
    main()