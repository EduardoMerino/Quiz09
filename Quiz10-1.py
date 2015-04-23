#functions:
def three_sum(l):
    n=0
    c=0
    for i in (l):
        if(i%3==0):
            n=n+i
            c=c+1
    return[n,c]
#code:
x=[3,9,6,5,4,2,1,11]
print(x)
y=three_sum(x)
print("La lisa tiene",y[-1],"numes divisibles entre 3")
print("La suma de esos numeros es: ",y[0])
