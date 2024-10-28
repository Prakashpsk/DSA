def get_union(a, b):
    i, j = 0, 0
    ans = []
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            if not ans or a[i] != ans[-1]:
                ans.append(a[i])
            i += 1
        else:
            if not ans or b[j] != ans[-1]:
                ans.append(b[j])
            j += 1
    while j < len(b):
        if not ans or b[j] != ans[-1]:
            ans.append(b[j])
        j += 1
    while i < len(a):
        if not ans or a[i] != ans[-1]:  
            ans.append(a[i])
        i += 1
    return ans

a=[1,1,2,2,3]
b=[1,2,3,4,5]
result= get_union(a, b)
for k in result:
    print(k, end=" ")

    #Time Complexity

#"m" is the length of a

#"n" is the length of b

#The while loops conclude when both i and j reach the ends of a and b

#TC = O(m + n)