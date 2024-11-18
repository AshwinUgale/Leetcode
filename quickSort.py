def quick_sort(arr):
    n = len(arr) 
    if n <=1:
        return arr
    else:
        pivot= arr.pop()

    i_greater = []
    i_lower = []
    for i in arr:
        if i > pivot:
            i_greater.append(i)
        else:
            i_lower.append(i)

    return quick_sort(i_lower) + [pivot] +quick_sort(i_greater)

print(quick_sort([34,2,52,54,25,222]))