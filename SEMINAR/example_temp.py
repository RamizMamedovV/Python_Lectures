def is_number(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def apply_operator(operators, operands):
    operator = operators.pop()
    right = operands.pop()
    if len(operands) !=0:
        left = operands.pop()
    else:
        left = 0    

    if operator == '*':
        operands.append(left * right)
    elif operator == '/':
        operands.append(left / right)
    elif operator == '+':
        operands.append(left + right)
    elif operator == '-':
        operands.append(left - right)

def evaluate_expression(expression):
    operators = []
    operands = []

    i = 0
    while i < len(expression):
        if expression[i] == ' ':
            i += 1
            continue
        elif expression[i] in '*/+-':
            operators.append(expression[i])
            i += 1
        elif expression[i] == '(':
            operators.append(expression[i])
            i += 1
        elif expression[i] == ')':
            while operators[-1] != '(':
                apply_operator(operators, operands)
            operators.pop()
            i += 1
        else:
            j = i
            while j < len(expression) and is_number(expression[j]):
                j += 1
            operands.append(int(expression[i:j]))
            i = j

    while operators:
        apply_operator(operators, operands)

    return operands[0]

list1 = '-1*12*(40+60)*(2+ 4)'
result = evaluate_expression(list1)
print(result)
