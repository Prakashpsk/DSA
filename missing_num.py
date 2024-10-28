def mising(arr):
    max=arr[0]
    for i in arr:
        if i > max:
            max=i

    min=arr[0]
    for i in arr:
        if i < min:
            min=i 
    miss=[]
    for num in range(min+1,max):
        if num not in arr:
            miss.append(num)
    return miss 

arr=[1,2,4,6,7,8,3]
print(mising(arr))
