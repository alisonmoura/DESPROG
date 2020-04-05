while(True):
    [n, m] = input().split()

    n = int(n)
    m = int(m)

    if(n == 0 and m == 0): exit()

    players_scores = {}
    players_guild = {}
    guilds_scores = {}
    guilds_win = {}

    scores = input().split()
    for i in range(n):
        players_scores[i+1] = int(scores[i])
        players_guild[i+1] = i+1
        guilds_scores[i+1] = int(scores[i])

    # print(players_scores, players_guild, guilds_scores)

    for i in range(m):
        [Q, A, B] = input().split()
        Q = int(Q)
        A = int(A)
        B = int(B)
        if(Q == 1):
            players_guild[B] = players_guild[A]
            del guilds_scores[B]
            guilds_scores[players_guild[A]] += players_scores[B]
            # print(players_guild, guilds_scores)
        elif(Q == 2):
            if guilds_scores[players_guild[A]] > guilds_scores[players_guild[B]]:
                if(players_guild[A] in guilds_win): guilds_win[players_guild[A]] += 1
                else: guilds_win[players_guild[A]] = 1
            elif guilds_scores[players_guild[B]] > guilds_scores[players_guild[A]]: 
                if(players_guild[B] in guilds_win): guilds_win[players_guild[B]] += 1
                else: guilds_win[players_guild[B]] = 1
            # print(guilds_win)
    if 1 in guilds_win: print(guilds_win[1])
    else: print(0)