while(True) :
    
    [h1,m1,h2,m2] = input().split()

    h1 = int(h1)
    m1 = int(m1)
    h2 = int(h2)
    m2 = int(m2)

    if (h1 == 0 and h2 == 0 and m1 == 0 and m2 == 0): exit()

    start = h1*60 + m1
    end = h2*60 + m2

    minutes = 0

    while(start != end):
        
        if(h1 == 23 and m1 == 59):
            h1 = 0
            m1 = 0
        elif(m1 == 59):
            h1 += 1
            m1 = 0
        else: m1 += 1

        minutes += 1
        start = h1*60 + m1

    print(minutes)
