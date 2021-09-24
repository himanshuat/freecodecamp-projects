def max_no_of_digits(a, b):
    if len(a) > len(b):
        return len(a)
    else:
        return len(b)

def arithmetic_arranger(problems, answers=False):

    # Too many problems
    if len(problems) > 5:
        return "Error: Too many problems."

    arranged_problems = ''
    first_line = ''
    second_line = ''
    dashed_line = ''
    answers_line = ''

    for problem in problems:
        
        # Check for '*' and '/'
        if '*' in problem or '/' in problem:
            return "Error: Operator must be '+' or '-'."
        
        # '25 + 14'
        # operand1 = '25', operator = '+', operand2 = '14'
        operand1, operator, operand2 = problem.split()

        # Check for valid operands
        if not all([operand1.isnumeric(), operand2.isnumeric()]):
            return "Error: Numbers must only contain digits."

        # Check for no. of digits in operands
        if not all([len(operand1) < 5, len(operand2) < 5]):
            return "Error: Numbers cannot be more than four digits."

        # Most no. of digits among operands
        max_length = max_no_of_digits(operand1, operand2)
        
        first_line += '  ' + (max_length - len(operand1)) * ' ' + operand1 + '    '
        second_line += operator + ' ' + (max_length - len(operand2)) * ' ' + operand2 + '    '
        dashed_line += (max_length + 2) * '-' + '    '

        if answers:
            ans = str(eval(problem))
            answers_line += ((max_length + 2) - len(ans)) * ' ' + ans + '    '

    # Strip the last 4 spaces
    arranged_problems = first_line.rstrip() + '\n' + second_line.rstrip() + '\n' + dashed_line.rstrip()

    if answers:
        arranged_problems += '\n' + answers_line.rstrip()

    return arranged_problems
