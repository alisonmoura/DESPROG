n = int(input())

for i in range(n):

    k = int(input())
    first_one = ""
    result = ""

    for j in range(k):
        if(first_one == ""):
            first_one = input()
        else: 
            new_one = input()
            if(new_one != first_one): result = 'ingles'
            # print(new_one, first_one)
    
    if(result == ""): print(first_one)
    else: print('ingles')