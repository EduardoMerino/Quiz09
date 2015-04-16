#funciones:
def superpower(a,b):
	ans=a
	for i in range (1,b):
		ans=ans*a
	return ans
#codigo:
x=int(input("Dame un número x: "))
n=int(input("elevado a la: "))
res=superpower(x,n)
print(x,"^",n," = ",res)

