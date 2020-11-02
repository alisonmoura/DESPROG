[a, b, c] = input().split()

a = float(a)
b = float(b)
c = float(c)

num_arr = [a, b, c]
num_arr.sort(reverse=True)

if num_arr[0] >= num_arr[1] + num_arr[2]:
    print("NAO FORMA TRIANGULO")
    exit()

if num_arr[0]**2 == num_arr[1]**2 + num_arr[2]**2:
    print("TRIANGULO RETANGULO")

if num_arr[0]**2 > num_arr[1]**2 + num_arr[2]**2:
    print("TRIANGULO OBTUSANGULO")

if num_arr[0]**2 < num_arr[1]**2 + num_arr[2]**2:
    print("TRIANGULO ACUTANGULO")

if num_arr[0] == num_arr[1] and num_arr[0] == num_arr[2] and num_arr[1] == num_arr[2]:
    print("TRIANGULO EQUILATERO")

if (num_arr[0] == num_arr[1] and num_arr[2] != num_arr[0]) or (num_arr[0] == num_arr[2] and num_arr[1] != num_arr[0]) or (num_arr[1] == num_arr[2] and num_arr[2] != num_arr[0]):
    print("TRIANGULO ISOSCELES")