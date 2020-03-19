tests_number = int(input())

for i in range(tests_number): 
    commad_number = int(input())
    commands = []
    p = 0

    for j in range(commad_number):
        command = input()
        if(command == "LEFT"): 
            commands.append(command)
            p -=1
        elif(command == "RIGHT"): 
            p +=1
            commands.append(command)
        else: 
            back_command = commands[int(command[len(command)-1])-1]
            commands.append(back_command)
            if(back_command == "LEFT"): p -=1
            elif(back_command == "RIGHT"): p +=1
    
    print(p)
