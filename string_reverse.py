def reversebyStack(s):
	
	stack = []

	for i in range(len(s)):
		stack.append(s[i])
	
	for i in range(len(s)):
		s[i] = stack.pop()
	print(s)
s= "fuck the"
s = list(s)
reversebyStack(s)
s= ''.join(s)
	

# o(n) O(n)