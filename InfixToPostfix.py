class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Pop from an empty stack")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Peek from an empty stack")

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

def isOp(c):
    op = ["+", "/", "*", "-", "^", "("]
    return c in op

def precedence(op):
    if op in ['*', '/']:
        return 2
    elif op in ['+', '-']:
        return 1
    elif op == '^':
        return 3
    else:
        return 0   # Lowest precedence for other characters

def infix_to_postfix(input_string):
    elements = []
    current_element = ""
    stack = Stack()

    for char in input_string:
        if isOp(char) or char == ")" or char == "(":
            if current_element:
                # Add the operand to the list before handling the operator, trim spaces just in case
                elements.append(current_element.strip())
                current_element = ""
            if char == "(":
                stack.push(char)
            elif char == ")":
                while not stack.is_empty() and stack.peek() != "(":
                    elements.append(stack.pop())
                if not stack.is_empty():
                    stack.pop()  # Pop the "("
            else:
                while not stack.is_empty() and stack.peek() != "(" and precedence(stack.peek()) >= precedence(char):
                    elements.append(stack.pop())
                stack.push(char)
        else:
            # Accumulate characters of the operand
            current_element += char

    # Add the last operand to the list, if any
    if current_element:
        elements.append(current_element.strip())

    # Empty the stack and append all operators to the elements list
    while not stack.is_empty():
        elements.append(stack.pop())

    # Directly join elements without adding spaces
    return "".join(elements)

# Test the function with a specific input string
input_string = "a ^ b ^ c"
postfix_expression = infix_to_postfix(input_string)
print(postfix_expression)
