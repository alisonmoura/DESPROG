n = -1

def factorial(n):
    mult = 1;
    for i in range(1, n+1):
        mult *= i;
    return mult;

def C(n, r):
    if n == r: return 1
    return factorial(n)/(factorial(r)*factorial(n-r))

while n != 0:
    n = int(input())
    if(n == 0): exit()
    count = 0
    for i in range(1, n+1):
        count += i*i
    print(int(count))

