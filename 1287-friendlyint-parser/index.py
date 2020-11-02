while(True):
    try:
        typed_in = input()
        typed_in = typed_in.replace(',','')
        typed_in = typed_in.replace(' ','')
        typed_in = typed_in.replace('l','1')
        typed_in = typed_in.replace('o','0')
        typed_in = typed_in.replace('O','0')
        
        parsed = int(typed_in)

        if(parsed > 2147483647): raise ValueError('Overflow do valor')

        print(parsed)
    
    except ValueError:
        print('error')

    except EOFError:
        exit()