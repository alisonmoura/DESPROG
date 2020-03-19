while(True):
    try:
        typed_in = input()
        home_pressed = False
        end_pressed = False
        result_text = ''
        temp_text = ''

        for i, e in enumerate(typed_in, start=1):

            if(e != '[' and e != ']'): 
                if(home_pressed or end_pressed):
                    temp_text += e
                else: result_text += e

            if(e == '[' or e == ']' or i == len(typed_in)):

                if(home_pressed):
                    result_text = temp_text + result_text
                
                if(end_pressed):
                    result_text = result_text + temp_text

                home_pressed = False
                end_pressed = False
                temp_text = ''

                if(e == '['): home_pressed = True
                else: end_pressed = True

        print(result_text)
    
    except EOFError:
        exit()