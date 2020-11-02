cases_number = int(input())

for i in range(cases_number):
    [A,D,B] = input()
    D_lower = D.lower()
    if (A == B): print(int(A)*int(B))
    elif(D == D_lower): print(int(A)+int(B))
    else: print(int(B)-int(A))