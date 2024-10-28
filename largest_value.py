def largest(arr,n):
    low=arr[0]
    for i in range(n):
        if arr[i]<arr[low]:
            low=arr[i]
    print(low)

    max=arr[0]
    for i in  range(n):
        if arr[i]>arr[max]:
            max=arr[i]
    print(max)


arr=[1,2,3,4,5]
n=len(arr)
largest(arr,n)


#time complexity O(n)
#space complexity o(1)
