def remove_dup(s1):
    n=len(s1)
    dict={}
    index=0
    ans=""
    for i in range(0,n):
        if s1[i] not in dict  or dict[s1[i]] ==0:
            s1[index]=s[i]
            print(s1[index],end=" ")
            index+=1 
            dict[s[i]]=1


s="kesavaa "
s1=list(s)
remove_dup(s1)