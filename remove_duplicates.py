def remove_duplicates(arr):
    n = len(arr)
    if n == 0 or n == 1:
        return n
    j = 0
    for i in range(n - 1):
        if arr[i] != arr[i + 1]:
            arr[j] = arr[i]
            j += 1

    arr[j] = arr[n - 1]
    
    return j + 1

    
arr = [1,1,1,2,2,2,3,4,5]
n = len(arr)
result = remove_duplicates(arr)
print("count:",result)
for i in range(result):
    print(arr[i],end=" ")

#O(n) O(1)