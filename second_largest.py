def second_largest_element(arr):
    #optimal sollution
    max=arr[0]
    s_l=-1
    for i in range(1,len(arr)):
        if arr[i]> max:
            s_l=max
            max=arr[i]
            if arr[i]> s_l and arr[i] < max:
                s_l=arr[i]
    return s_l
arr=[1,2,3,4,22,45]
result = second_largest_element(arr)
if result != -1:
    print(result)


#time complexity O(n)
#O(1)