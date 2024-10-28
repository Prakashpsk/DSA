def rotation(arr,k):
    arr[:k]=reversed(arr[:k])
    arr[k:]=reversed(arr[k:])
    arr[:]=reversed(arr)


arr=[1,2,3,4,5]
k=2
rotation(arr,k)
print(arr)


