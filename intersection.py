def intersection(a, b):
    ans = []
    i, j = 0, 0
    m, n = len(a), len(b)
    while i < m and j < n:
        if a[i] == b[j]:
            ans.append(a[i])
            i += 1
            j += 1
        elif a[i] < b[j]:
            i += 1
        else:
            j += 1
    return ans

a=[1,2,3]
b=[1,2,4]
ans = intersection(a, b)
print(*ans)

#time complexity O(m+n)