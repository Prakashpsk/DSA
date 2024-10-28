def zeros_to_end(arr):

    i=0
    for j in range(len(arr)):
        if arr[j]!=0:
            arr[i],arr[j]=arr[j],arr[i]
            i+=1 
    return j
arr=[0,0,0,2,1,0,2,0,44,1]
result=zeros_to_end(arr)
print(result)
for i in range(result):
    print(arr[i],end=" ")

# O(n) O(1)