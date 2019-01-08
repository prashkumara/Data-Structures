def selectionSort(arr,n):

    for i in range(0,n-1):
        imin=i

        for j in range(i,n):
            if arr[j] < arr[imin]:
                imin=j

        temp=arr[i]
        arr[i]=arr[imin]
        arr[imin]=temp
    return(arr)


arr=[6,4,8,2,9,1]
output=selectionSort(arr,len(arr))
print(output)

# time complexity   Worst case: O(n^2)