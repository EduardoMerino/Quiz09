#Functions
def dotProduct(x,y):
    if ((len(x))==(len(y))):
        n=0
        for i in range(0,(len(x))):
            n=n+((x[i])*(y[i]))
    else:
            n=str("none")
    return(n)

#code:
v1=[5,2,4]
v2=[6,9,7]
r=dotProduct(v1,v2)
print(v1)
print(v2)
print(r)
