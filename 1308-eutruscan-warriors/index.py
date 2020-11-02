n = int(input())

for i in range(n):
    troop_count = int(input())

    no_more_than = troop_count
    no_less_than = 0

    line_count = troop_count
    line_min =  int(line_count * (1 + line_count)/2) # soma dos termos de uma P.A

    while True: 
        # print('Linha: %d - min: %d - tropas: %d' % (line_count, line_min, troop_count))
        # 8 < 10 

        if(troop_count == line_min):
            break
        elif(troop_count > line_min and no_more_than - line_count == 1):
            break
        elif(troop_count < line_min):
            no_more_than = line_count
        elif(troop_count > line_min): 
            no_less_than = line_count
        else: print("Caiu no else")
        
        line_count = int((no_more_than + no_less_than)/2)
        line_min =  int(line_count * (1 + line_count)/2)

    print(line_count)