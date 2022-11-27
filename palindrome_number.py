'''
Given an integer x, return true if x is a 
palindrome
, and false otherwise.
'''
def is_palindrime(x):
	return x > 0 and x == int(str(x)[::-1])

def is_palindrime_without_string(x):
	if x < 0: return False
	r = []
	while x:
		r.append(x % 10)
		x //= 10
	return r == r[::-1]
print(is_palindrime(121))
print(is_palindrime_without_string(12321))