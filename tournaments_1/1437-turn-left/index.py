while(True):
    n = int(input())

    if(n == 0): exit()

    commands = input()
    positions = ['O','N','L','S']
    actual_pos = 1

    for c in commands: 
        if(c == "D"): actual_pos += 1
        elif(c == "E"): actual_pos -= 1

        if(actual_pos < 0): actual_pos = 3
        if(actual_pos > 3): actual_pos = 0

    print(positions[actual_pos])