def reverse(arr):
    left=0
    right=len(arr)-1

    while left < right:
        temp=arr[left]
        arr[left]=arr[right]
        arr[right]=temp
        left +=1
        right-=1
    return arr

arr=[1,2,3,4]   
print(reverse(arr))


def sort(arr):
    l=0 
    r=len(arr)-1
    
arr=[1,2,3,4]   
print(sort(arr))
