total_joined = int(input())
votes = input().split()
yes_votes = 0
no_votes = 0

for v in votes:
    if v == "0": yes_votes += 1
    else: no_votes += 1

if yes_votes > no_votes: 
    print("Y")
else: print("N")