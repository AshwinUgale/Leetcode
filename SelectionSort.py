def selection_sort(arr):
    n = len(arr)
    for i in range(n-1):
        mini = i
        for j in range(i+1,n):
            if arr[j]<arr[mini]:
                mini=j
        arr[i],arr[mini]= arr[mini],arr[i]
    return arr

print(selection_sort([52,51,22,5,12]))