even_count = 0
odd_count = 0
positive_count = 0
negative_count = 0

a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

num_arr = [a, b, c, d, e]

for i in num_arr:
    if i%2 ==0: even_count += 1
    else: odd_count += 1
    
    if i > 0: positive_count += 1
    if i < 0: negative_count += 1

print(even_count, "valor(es) par(es)")
print(odd_count, "valor(es) impar(es)")
print(positive_count, "valor(es) positivo(s)")
print(negative_count, "valor(es) negativo(s)")