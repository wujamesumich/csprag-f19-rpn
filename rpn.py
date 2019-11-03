#!/usr/bin/env python3

def calculate(arg):
    #pass
    stack = list()
    # range based for
    for token in arg.split():
        print(token)
        if token == '+':
            arg2 = stack.pop()
            arg1 = stack.pop()
            result = arg1 + arg2
            stack.append(result)
        elif token == '-':
            arg2 = stack.pop()
            arg1 = stack.pop()
            result = arg1 - arg2
            stack.append(result)
        # ADDED HW8 -----
        elif token == '*':
            arg2 = stack.pop()
            arg1 = stack.pop()
            result = arg1 * arg2
            stack.append(result)
        elif token == '/':
            arg2 = stack.pop()
            arg1 = stack.pop()
            result = arg1 / arg2
            stack.append(result)
        elif token == '^':
            arg2 = stack.pop()
            arg1 = stack.pop()
            result = arg1 * arg2
            stack.append(result)
        # ---------------
        else:
            stack.append(int(token))

        #print(stack)
        if len(stack) != 1:
            raise TypeError('malformed input')


def main():
    while True:
            calculate(input("rpn calc> "))

if __name__ == '__main__': # Note: that's "underscore underscore n a m e ..."
    main()