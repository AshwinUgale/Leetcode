def bubble_sort(arr):
    sorted = False
    while not sorted:
        sorted = True
        for i in range(0, len(arr)-1):
            if arr[i]>arr[i+1]:
                sorted= False
                arr[i],arr[i+1]=arr[i+1],arr[i]
    return arr

print(bubble_sort([25,66,22,5,2,634554]))