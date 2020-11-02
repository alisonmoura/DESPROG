n = int(input())

precedence = {
    '^': 3,
    '/': 2,
    '*': 2,
    '-': 1,
    '+': 1
}

def not_a_operator(e):
    result = True
    if(e == '('): result = False
    if(e == ')'): result = False
    if(e == '^'): result = False
    if(e == '/'): result = False
    if(e == '*'): result = False
    if(e == '+'): result = False
    if(e == '-'): result = False
    return result

for i in range(n):
    
    exp = input()
    stack = []
    result = ''
    # last_pos = -1

    for e in exp:

        # print('letter:', e)
        # print('last_pos:', last_pos)
        # if(len(stack) > 0): print('last on stack:', stack[-1])
        # if(e != ')' and e != '(' and not not_a_operator(e)): print('precedence: ', precedence[e])
        # if(len(stack) > 0 and stack[-1] != ')' and stack[-1] != '(' and not not_a_operator(stack[-1])): print('precedence of the last: ', precedence[stack[-1]])
        # if(e != ')' and e != '(' and not not_a_operator(e) and last_pos >= 0 and stack[last_pos] != ')' and stack[last_pos] != '(' and not not_a_operator(stack[last_pos])): print('precedences compare: ', precedence[e] <= precedence[stack[last_pos]])

        if(not_a_operator(e)):
            result += e

        elif(e == '('):
            stack.append(e)

        elif(e == ')'):

            while(stack or stack[-1] != '('):
                poped = stack.pop()
                if(poped == '('):
                    break
                result += poped
        
        elif(len(stack) > 0 and stack[-1] != '(' and int(precedence[e]) > int(precedence[stack[-1]])):
            stack.append(e)

        elif(len(stack) > 0):
            while(stack and stack[-1] != '(' and int(precedence[e]) <= int(precedence[stack[-1]])):
                poped = stack.pop()
                if(poped == '('):
                    break
                result += poped
            stack.append(e)
        
        else: stack.append(e)

        # print('result:', result)
        # print('stack:', stack)
    
    while(stack):
        poped = stack.pop()
        result += poped

    print(result)
