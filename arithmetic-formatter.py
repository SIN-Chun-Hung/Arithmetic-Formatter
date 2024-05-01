import re

def arithmetic_arranger(problems, show_answers=False):

    if len(problems) > 5:
        return 'Error: Too many problems.'

    num_regex = "\d+"
    operators_regex = "[+\-*/]+"

    inorder_problems_operands = []
    inorder_problems_operators = []

    for problem in problems:
        inorder_problems_operands.append(re.findall(num_regex ,problem))
        inorder_problems_operators.append(re.findall(operators_regex ,problem))

    for operator in inorder_problems_operators:
        if operator[0] == '*' or operator[0] == '/':
            return "Error: Operator must be '+' or '-'."

    for operands in inorder_problems_operands:
        if len(operands) > 2 or len(operands) < 2:
            return 'Error: Numbers must only contain digits.'

        for operand in operands:
            if len(operand) > 4:
                return  'Error: Numbers cannot be more than four digits.'

    operator_to_operand_space = ' '
    operator_space = ' '
    problem_separation_space = ' ' * 4
    dash = '-'
    output_first_row = ''
    output_second_row = ''
    output_third_row = ''
    answer_row = ''

    first_operand = [i[0] for i in inorder_problems_operands]
    second_operand = [i[1] for i in inorder_problems_operands]
    first_operand_length = [len(i[0]) for i in inorder_problems_operands]
    second_operand_length = [len(i[1]) for i in inorder_problems_operands]
    answer = []

    for num_problem in range(len(problems)):
        if first_operand_length[num_problem] - second_operand_length[num_problem] < 0:
            output_first_row = output_first_row + operator_space + operator_to_operand_space + ' ' * abs(first_operand_length[num_problem] - second_operand_length[num_problem]) + first_operand[num_problem] + problem_separation_space

            output_second_row = output_second_row + inorder_problems_operators[num_problem][0] + operator_to_operand_space + second_operand[num_problem] + problem_separation_space

        elif first_operand_length[num_problem] - second_operand_length[num_problem] == 0:
            output_first_row = output_first_row + operator_space + operator_to_operand_space + first_operand[num_problem] + problem_separation_space

            output_second_row = output_second_row + inorder_problems_operators[num_problem][0] + operator_to_operand_space + second_operand[num_problem] + problem_separation_space

        else:
            output_first_row = output_first_row + operator_space + operator_to_operand_space + first_operand[num_problem] + problem_separation_space

            output_second_row = output_second_row + inorder_problems_operators[num_problem][0] + operator_to_operand_space + ' ' * abs(first_operand_length[num_problem] - second_operand_length[num_problem]) + second_operand[num_problem] + problem_separation_space

        output_third_row = output_third_row +  dash * (2 + max(first_operand_length[num_problem], second_operand_length[num_problem])) + problem_separation_space

        if inorder_problems_operators[num_problem][0] == '+':
             answer.append(str(int(first_operand[num_problem]) + int(second_operand[num_problem])))
        else:
             answer.append(str(int(first_operand[num_problem]) - int(second_operand[num_problem])))

        answer_row = answer_row + ' ' * (len(operator_space) + len(operator_to_operand_space) + max(first_operand_length[num_problem], second_operand_length[num_problem]) - len(answer[num_problem])) + answer[num_problem] + problem_separation_space

        if num_problem == len(problems) - 1:
            output_first_row = output_first_row.rstrip()
            output_second_row = output_second_row.rstrip()
            output_third_row = output_third_row.rstrip()
            answer_row = answer_row.rstrip()

    if show_answers == True:
        return output_first_row + '\n' + output_second_row + '\n' + output_third_row + '\n' + answer_row
    else:
        return output_first_row + '\n' + output_second_row + '\n' + output_third_row



print(f'\n{arithmetic_arranger(["3 / 855", "3801 - 2", "45 + 43", "123 + 49"], True)}')
