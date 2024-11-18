def insertionSort(arr):
    for i in range(1, len(arr)):
        while arr[i-1]>arr[i] and i>0:
            arr[i-1],arr[i]= arr[i],arr[i-1]
            i=i-1
    return arr

print(insertionSort([24,2,52,55,13]))