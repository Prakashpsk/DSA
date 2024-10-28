def linear_search(arr, k):
    for i in range(len(arr)):
        if arr[i] == k:
            return i
    return -1

n, k = map(int, input().split())
arr = list(map(int, input().split()))
print(linear_search(arr, k))