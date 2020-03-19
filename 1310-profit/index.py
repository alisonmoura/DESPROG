# Kadane's Algorithm

while(True):

    try:
        typed_in = input()
        if(typed_in == ''): exit()
        num_days = int(typed_in)
        cost_per_day = int(input())
        revenues = []

        for i in range(num_days):
            revenues.append(int(input())-cost_per_day)

        max_total = 0
        max_local = 0

        for i in range(len(revenues)):
            max_local = max_local + revenues[i]
            if(max_total < max_local):
                max_total = max_local
            if(max_local < 0):
                max_local = 0
            
        print(max_total)
    except EOFError:
        exit()