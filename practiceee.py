def reverse(s):
    return ' '.join(s.split()[::-1])

s="prakash picchamuthu"
print(reverse(s)) 
"""def reverse(s):
    str = ""
    for i in s:
        str = i + str
    return str

s = "kesavs"

print("The original string is : ", end="")
print(s)

print("The reversed string(using loops) is : ", end="")
print(reverse(s))"""
