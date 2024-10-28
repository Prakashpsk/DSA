def selectionsort(arr):
    for i in range(len(arr)):
        min=i
        for j in range(i,len(arr)):
            if(arr[j]<arr[min]):
                min=j 
        arr[i],arr[min]=arr[min],arr[i]

arr=[6,4,2,1,45,22]
selectionsort(arr)
print(arr)

# time complexity O(n*2)