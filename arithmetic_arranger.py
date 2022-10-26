from pytest import main
import re
# Run unit tests automatically
def arithmetic_arranger(problem, solve = False):
    if len(problem) > 5:
        print("Error: Too many problems")

    op1 = " "
    op2 = " "
    lines = " "
    total = " "
    for i in problem:
        if re.search("[*] | [/]", i):
            if re.search("[a-zA-Z]", i):
                return "Error: Numbers must only contain digits."
            return "Error: Operator must be '+' or '-'."

        if re.search("[0-9]{5}", i):
            return "Error: Numbers cannot be more than four digits."

        first_number = i.split(" ")[0]
        operator = i.split(" ")[1]
        scd_number = i.split(" ")[2]
        sum = " "
        if operator == "+":
            sum = str(int(first_number) + int(scd_number))
        else:
            sum = str(int(first_number) - int(scd_number))

        length = max(len(first_number), len(scd_number)) + 2
        top = str(first_number).rjust(length)
        bottom = operator + str(scd_number).rjust(length - 1)
        line = ""
        res = str(sum).rjust(length)
        for l in range(length):
            line += "-"

        if problem != problem[-1]:
            op1 += top + '  '
            op2 += bottom + '  '
            lines += line + '  '
            total += res + '  '
        else:
            op1 += top
            op2 += bottom
            lines += line
            total += res

    if solve:
        string = op1 + "\n" + op2 + "\n" + lines + "\n" + total
    else:
        string = op1 + "\n" + op2 + "\n" + lines + "\n" + total
    return string
  
print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))