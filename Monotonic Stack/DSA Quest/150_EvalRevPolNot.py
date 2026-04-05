#tokens = ['2','1','+','3','*']
tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]

def evalRPN(tokens):
    stack = []
    for t in tokens:
        if t not in '+-/*':
            stack.append(int(t))
        else:
            r, l = stack.pop(), stack.pop()
            if t == '+': stack.append(l + r)
            elif t == '-': stack.append(l - r)
            elif t == '*': stack.append(l * r)
            elif t == '/': stack.append(int(l/r))
    return stack[0]
    
print(evalRPN(tokens))