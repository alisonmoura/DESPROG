while(True):
    try:
        typed_in = input().lower().split()
        last_word = ""
        last_alliteration = ""
        count = 0

        for word in typed_in:
            if(last_word != ""):
                if(last_word[0] == word[0]):
                    if(last_alliteration == ""):
                        last_alliteration = word[0]
                        count += 1
                else: last_alliteration = ""
            last_word = word
        
        print(count)

    except EOFError:
        exit()