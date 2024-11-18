def rec_bubble_sort(arr, n = None):
    if n is None:
        n = len(arr)

    if n ==1:
        return
    
    for i in range(n-1):
        if arr[i]>arr[i+1]:
            arr[i],arr[i+1]=arr[i+1],arr[i]
        
    rec_bubble_sort(arr,n-1)
    return arr

print(rec_bubble_sort([13,52,66,22,2,62]))