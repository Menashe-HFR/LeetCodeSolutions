'''
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two 
preceding ones, starting from 0 and 1. That is, Given n, calculate F(n).
'''

# def fib(n):
# 	f = [0,1]
# 	for i in range(1,n):
# 	    f.append(f[i] + f[i-1])
# 	return f[n]

def fibo(n):
	f = [0,1]
	if n ==0:
		return 0

	for i in range(1,n):
		temp = f[0]
		f[0] = f[1]
		f[1] = (f[0]+temp)

	return f[1]

print(fibo(5))