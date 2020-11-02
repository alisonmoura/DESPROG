# 6\n100 150 1.0 0\n90000 120000 5.5 3.5\n56700 72000 5.2 3.0\n123 2000 3.0 2.0\n100000 110000 1.5 0.5\n62422 484317 3.1 1.0\n

typed_in = input()
print(typed_in.split('\\n'))
tests_number = int(input())

# for i in range(tests_number):
#     [pa, pb, ga, gb] = input().split()
    
#     pa = int(pa)
#     pb = int(pb)
#     ga = float(ga)
#     gb = float(gb)

#     years = 0

#     while pa <= pb:
#         pa += round(pa*(ga/100))
#         pb += round(pb*(gb/100))
#         years += 1
#         if(years > 100):
#             print("Mais de 1 seculo.")
#             break
#         print(pa, pb, years)

#     if(years <= 100): print(years, "anos.")