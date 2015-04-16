#funciones:
def pit (x1,y1,x2,y2):
	i=-x1+x2
	j=-y1+y2
	ans=((i**2)+(j**2))**0.5
	return ans
#codigo:
x1=float(input("Dame un número x1: "))
y1=float(input("Dame un número y1: "))
x2=float(input("Dame un número x2: "))
y2=float(input("Dame un número y2: "))
dist=pit(x1,y1,x2,y2)
print("la distancia entre esos puntos es: ",dist)
