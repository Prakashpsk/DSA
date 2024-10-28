def merge(arr_1,arr2,arr_3,n1,n2):
    arr_1.sort()
    arr_2.sort()
    i,j,k=0,0,0 

    while i< n1 and j < n2:
        if arr_1[i] < arr_2[j]:
            arr_3.insert(k,arr_1[i])
            i+=1
            k+=1
        else:
            arr_3.insert(k,arr_2[j])
            j+=1
            k+=1
    while i< n1:
        arr_3.insert(k,arr_1[i])
        i+=1
        k+=1
    while j < n2:
        arr_3.insert(k,arr_2[j])
        j+=1
        k+=1

    return arr_3


arr_1=[1,2,3,4,1,3]
arr_2=[5,6,7,8]
arr_3=[]
n1=len(arr_1)
n2=len(arr_2)
res=merge(arr_1,arr_2,arr_3,n1,n2)
print(res)