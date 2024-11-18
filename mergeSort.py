def merge_sort(arr):
    if len(arr)>1:
        leftArr= arr[:len(arr)//2]
        rightArr= arr[len(arr)//2:]

        merge_sort(leftArr)
        merge_sort(rightArr)

        i=0
        j=0
        k=0
        while i < len(leftArr) and j <len(rightArr):
            if leftArr[i] < rightArr[j]:
                arr[k] = leftArr[i]
                i=i+1
            else:
                arr[k]=rightArr[j]
                j=j+1
            k=k+1

        while i < len(leftArr):
            arr[k]=leftArr[i]
            i=i+1
            k=k+1
        while j < len(rightArr):
            arr[k]=rightArr[j]
            j=j+1
            k=k+1
    
    return arr

print(merge_sort([34,55,22,66,11,4,145,51]))