def insertionsort(arr):
    for i in range(1,len(arr)):
        j=i
        for j in range(j ,len(arr)):
            while arr[j-1]>arr[j] and j>0:
                arr[j-1],arr[j]=arr[j],arr[j-1]
                j-=1

arr=[6,4,3,2,1]
insertionsort(arr)
print(arr)

#time complexity O(n)