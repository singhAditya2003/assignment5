def reverse(s):
	if len(s) == 0:
		return s
	else:
		return reverse(s[1:]) + s[0]

a=input("enter string")
print(reverse(a))
