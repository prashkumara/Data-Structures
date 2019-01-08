def quickSort(arr,start,end):

    if start<end:
        pIndex = Partition(arr,start,end)
        quickSort(arr,0,pIndex-1)
        quickSort(arr,pIndex+1,end)
    return arr

def Partition(arr,start,end):
    pivot=arr[end]
    pIndex=start

    for i in range(start,end):
        if arr[i]<= pivot:
            temp=arr[i]
            arr[i]=arr[pIndex]
            arr[pIndex]=temp

            pIndex+=1
    temp=arr[pIndex]
    arr[pIndex]=arr[end]
    arr[end]=temp
    return pIndex


arr=[15,200,31,0,-1,6,3,9,1,7,2]
end=len(arr)
output=quickSort(arr,0,end-1)
print(arr)

# time complexity    Best/average case: O(n log n)
# time complexity   Worst case: O(n^2)