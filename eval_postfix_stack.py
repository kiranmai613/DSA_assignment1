#Evaluate a postfix expression using stack

def evaluate_postfix_expression(expression):
    stack = []

    # iterate over each character in the expression
    for char in expression:
        # if character is a digit, push onto stack
        if char.isdigit():
            stack.append(int(char))
        else:
            # if character is an operator, pop two operands from stack and apply operator
            operand2 = stack.pop()
            operand1 = stack.pop()
            result = 0
            
            if char == "+":
                result = operand1 + operand2
            elif char == "-":
                result = operand1 - operand2
            elif char == "*":
                result = operand1 * operand2
            elif char == "/":
                result = operand1 / operand2

            # push result onto stack
            stack.append(result)

    # the final result will be left on the stack
    return stack.pop()


expression = '34+5*9*'
result = evaluate_postfix_expression(expression)
print(result)  # Output: 35
