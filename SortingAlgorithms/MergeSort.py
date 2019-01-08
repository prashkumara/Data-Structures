def merge(left,right,arr):
    i=j=k=0
    leftlen=len(left)
    rightLen=len(right)

    while i<leftlen and j<rightLen:

        if left[i]<=right[j]:
            arr[k]=left[i]
            i+=1
        else:
            arr[k] = right[j]
            j+=1
        k+=1

    while i<leftlen:
        arr[k] = left[i]
        i+=1
        k+=1

    while j<rightLen:
        arr[k] = right[j]
        j+=1
        k+=1

def mergeSort(arr):
    arrLen=len(arr)
    if arrLen<2:
        return
    mid=arrLen//2
    left = [None] * mid
    right = [None] * (arrLen - mid)

    for i in range(0,mid):
        #print(arr[i],i)
        left[i] = arr[i]

    for i in range(mid,arrLen):
        #print(arr[i], i)
        right[i-mid] = arr[i]

    mergeSort(left)
    mergeSort(right)
    merge(left,right,arr)

    return(arr)

arr=[7,2,9,4,12,10,21,0,1]
print(arr)
output=mergeSort(arr)
print(output)

#space complexity: O(n)
#time complexity: O(n log n)