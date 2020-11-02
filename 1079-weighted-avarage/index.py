
count = int(input())

p1 = 2
p2 = 3
p3 = 5

for i in range(count):
    [a, b, c] = input().split()

    a = float(a)
    b = float(b)
    c = float(c)

    w_avarage = (p1*a+p2*b+p3*c)/(p1+p2+p3)
    print(round(w_avarage, 1))