#s="I Like"
#n=s.split()[::-1]
#print(' '.join(n))

"""def reverse(s):
    word=s.split('.')
    reverse_word=word[::-1]
    reverse_string=','.join(reverse_word)
    return reverse_string
s="I.like.program.very.much"
print(reverse(s)) 
"""

def reverse(s):
    str = ""
    for i in s:
        str = i + str
    return str

s = "katammagari kesava"
print(reverse(s))
