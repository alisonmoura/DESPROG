import math  

phi = 1.6180339887
psi = 0.6180339887*-1

def fibonacci(n): 
    return (round(math.pow(phi,n), 1) - round(math.pow(psi,n), 1))/round(math.sqrt(5), 1) # Binet's formula
    # result = 0
    # before_last = 1
    # last = 2
    # if(n == 1): return 1
    # if(n == 2): return 2
    # for i in range(3, n+1):
    #     result = last + before_last
    #     last = i
    #     before_last = i-1
    # return result

def get_inputs():
    [a, b] = input().split()
    a = int(a)
    b = int(b)
    return [a, b]

[a, b] = get_inputs()

while(a != 0 and b != 0):
    print(a,b)
    print(fibonacci(a))
    print(fibonacci(b))
    [a, b] = get_inputs()