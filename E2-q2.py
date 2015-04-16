#funciones:
def tri(x):
	for i in range (1,x):
		print("T"*i)
	for i in range (x,0,-1):
		print("T"*i)
	
#codigo:
x=int(input("Dame un número x: "))
tri(x)
