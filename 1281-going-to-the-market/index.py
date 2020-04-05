n = int(input())

for i in range(n):
    total = 0
    menu_map = {}
    list_map = {}
    
    menu_itens_count = int(input())

    for j in range(menu_itens_count):
        [ name, price ] = input().split()
        menu_map[name] = float(price)
    
    list_itens_count = int(input())

    for j in range(list_itens_count):
        [ name, quantity ] = input().split()
        list_map[name] = int(quantity)
    
    for item in list_map:
        total += menu_map[item] * list_map[item]

    print("R$ %.2f" % total)
