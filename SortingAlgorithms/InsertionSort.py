def insertionSort(arr,n):

    for i in range(1,n):
        key=arr[i]
        j=i-1

        while arr[j]>key and j>=0:
            arr[j+1]=arr[j]
            j=j-1

        arr[j+1]=key

    return(arr)


arr=[5,4,8,7,1,0]
output=insertionSort(arr,len(arr))
print(output)

# time complexity    Best case: O(n)
# time complexity   Worst case: O(n^2)