while(True):
    try:
        typed_in = input()
        lower = typed_in.replace(' ', '').lower()
        upper = typed_in.replace(' ', '').upper()
        result = ""
        pos = 0
        
        # print(typed_in, lower, upper)
        
        for s in typed_in:
            if(s == ' '): result += ' '
            else:
                if(pos%2 == 0): result += upper[pos]
                else: result += lower[pos]
                pos += 1

        print(result)

    except EOFError:
        exit()