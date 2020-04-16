def merge(arr, start, middle, end):
    aux = arr[start:end]
    i = start
    j = middle + 1
    k = start

    while i <= middle and j <= end:
        if aux[i] <= aux[j]:
            arr[k] = aux[i]
            k += 1
            i += 1
        else: 
            arr[k] = aux[j]
            k += 1
            j += 1
    
    while i <= middle:
        arr[k] = aux[i]
        k += 1
        i += 1

def merge_sort(arr, start, end):
    if start < end:
        middle = (start+end)/2
        merge_sort(arr, start, middle)
        merge_sort(arr, middle+1, end)
        
        merge(arr, start, middle, end)

n = int(input())
evens = []
odds = []

for i in range(n):

    typed_in = int(input())
    if typed_in % 2 == 0:
        evens.append(typed_in)
    else: odds.append(typed_in)

print(evens)
merge_sort(evens, 0, len(evens)-1)
print(evens)