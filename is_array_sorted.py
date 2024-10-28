def is_array_sorted(arr):
    for i in range(len(arr)):
        if arr[i]> arr[i+1]:
            return False 
    return True



arr=[14,5,2,2,34,1]
result=is_array_sorted(arr)
if result:
    print (1)
else:
    print (0)