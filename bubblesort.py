def bubblesort(arr):
    for i in range(len(arr)-1,0,-1):
        for j in range(i):
            if arr[j]> arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

arr=[6,2,3,1,66,32]
bubblesort(arr)
print(arr)


#time complexity is O(n*2)