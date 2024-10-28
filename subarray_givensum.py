def subarraywith(arr,l,sum):
    for i in range(1,l):
        currsum=arr[i]
        if currsum == sum:
            print("sum found in iindex",i)
            return 
        else:
            for j in range(i+1,l):
                currsum+=arr[j]
                if currsum== sum:
                    print("index found at",i,j)
                    return 

    print("no subarray found")


arr=[1,2,3,4,5,6]
l=len(arr)
sum=11
subarraywith(arr,l,sum)
