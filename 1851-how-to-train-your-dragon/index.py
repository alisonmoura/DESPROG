from heapq import heappush, heappop

TIME_POS = 1
FINE_POS = 2
DAYS_LEFT_POS = 3

lodging = []
current_day = 1
total_fine = 0
trainning_dragon = None
last_dragon = None

while(True):
    try:
        
        typed_in = input()
        if(typed_in == '-1'): raise EOFError()
        [T, F] = typed_in.split()
        T = int(T)
        F = int(F)
        FT = T/F
        heappush(lodging, (FT, T, F, T))

        current_day += 1
        if(trainning_dragon != None and trainning_dragon[DAYS_LEFT_POS] <= 0):
            last_dragon = trainning_dragon
            trainning_dragon = list(heappop(lodging))
            print(current_day - last_dragon[TIME_POS], trainning_dragon[FINE_POS])
            total_fine += trainning_dragon[FINE_POS] * (current_day - last_dragon[TIME_POS])
        elif(trainning_dragon == None): trainning_dragon = list(heappop(lodging))
        
        trainning_dragon[DAYS_LEFT_POS] -= 1

        print("Current Day:", current_day)
        print("Training dragon:", trainning_dragon)
        print("Last dragon:", last_dragon)
        print("Lodging:", lodging)
        print("Total fine:", total_fine)

    except EOFError:
        while(lodging):
            current_day += 1
            if(trainning_dragon != None and trainning_dragon[DAYS_LEFT_POS] <= 0):
                last_dragon = trainning_dragon
                trainning_dragon = list(heappop(lodging))
                print(current_day - last_dragon[TIME_POS], trainning_dragon[FINE_POS])
                total_fine += trainning_dragon[FINE_POS] * (current_day - last_dragon[TIME_POS])
            elif(trainning_dragon == None): trainning_dragon = list(heappop(lodging))
            
            trainning_dragon[DAYS_LEFT_POS] -= 1

            print("Current Day:", current_day)
            print("Training dragon:", trainning_dragon)
            print("Last dragon:", last_dragon)
            print("Lodging:", lodging)
            print("Total fine:", total_fine)
        
        print(total_fine)
        exit()