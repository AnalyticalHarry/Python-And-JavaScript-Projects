def arithmetic_arranger(problems, show_answers=False):
    #number of problems exceeds the limit
    if len(problems) > 5:
        return "Error: Too many problems."

    top_line = []
    bottom_line = []
    dash_line = []
    answer_line = [] 

    for problem in problems:
        elements = problem.split()

        operand1 = elements[0]
        operator = elements[1]
        operand2 = elements[2]

        #operator is valid
        if operator not in ["+", "-"]:
            return "Error: Operator must be '+' or '-'."

        #both operands contain only digits
        if not operand1.isdigit() or not operand2.isdigit():
            return "Error: Numbers must only contain digits."

        #operands have more than four digits
        if len(operand1) > 4 or len(operand2) > 4:
            return "Error: Numbers cannot be more than four digits."

        #maximum width required for alignment
        width = max(len(operand1), len(operand2)) + 2

        #arrange the top, bottom, and dash lines
        top_line.append(operand1.rjust(width))
        bottom_line.append(operator + operand2.rjust(width - 1))
        dash_line.append("-" * width)

        if show_answers:
            if operator == "+":
                answer = str(int(operand1) + int(operand2))
            else:
                answer = str(int(operand1) - int(operand2))
            answer_line.append(answer.rjust(width))

    #combine lines to form the arranged problems
    arranged_problems = [
        "    ".join(top_line),
        "    ".join(bottom_line),
        "    ".join(dash_line)
    ]

    if show_answers:
        arranged_problems.append("    ".join(answer_line)) 

    return "\n".join(arranged_problems)

print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True))
print()
print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))
