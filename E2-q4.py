#funcion:
def fibonacci(n):
	if (n==0 or n==1):
		return n
	else:
		a=0
		b=1
		c=1
		for i in range (1,n):
			c=a+b
			a=b
			b=c
	return c
#Code:
x1=int(input("Dame un número: "))
ans=fibonacci(x1)
print(ans)

