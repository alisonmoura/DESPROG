while(True):
    try:
        expression = input()
        stack = []
        incorrect = False

        for e in expression:
            
            if(e == '('):
                stack.append("(")

            elif(e == ')'):
                if(stack):
                    stack.pop()
                else: 
                    incorrect = True
            
        if(not stack and not incorrect):
            print('correct')
        else: print('incorrect')

    except EOFError:
        exit()