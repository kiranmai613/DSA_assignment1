#Reverse a string using a stack data structure

def reverse_string(string):
    stack = []
    # push each character onto the stack
    for char in string:
        stack.append(char)

    # pop each character from the stack and build the reversed string
    reversed_string = ""
    while len(stack) != 0:
        reversed_string += stack.pop()

    return reversed_string

string = "hello world"
reversed_string = reverse_string(string)
print(reversed_string)
