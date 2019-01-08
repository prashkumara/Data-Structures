def bubbleSort(arr,n):

    for i in range(0,n):
        flag=0

        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                temp=arr[j+1]
                arr[j+1]=arr[j]
                arr[j]=temp
                flag=1

        if flag==0:
            return arr

    return (arr)


arr=[6,3,9,1,7,2]
output=bubbleSort(arr,len(arr))
print(arr)

# time complexity   Worst case: O(n^2)