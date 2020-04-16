def shuffle(list):
    middle_index = int(len(list)/2)
    first_half = list[:middle_index]
    second_half = list[middle_index:]
    result = []

    for i in range(middle_index):
        result.append(second_half.pop(0))
        result.append(first_half.pop(0))

    return result

while(True):
    try:
        n = int(input())
        original = list(range(n))
        count = 0

        shuffled = shuffle(original)
        count += 1
    
        while(shuffled != original):
            shuffled = shuffle(shuffled)
            count += 1

        print(count)

    except EOFError:
        exit()