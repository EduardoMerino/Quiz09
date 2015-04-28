txt=open("random_numbers.txt","r")
#fuctions
def my_sum(l):
    n=0
    r=0
    while n<len(l):
        r=r+(l[n])
        n=n+1
    return r
def my_st(l):
    n=0
    r=0
    while n<len(l):
        r=((l[n])-(my_sum(l))/(len(l)))**2
        n=n+1
    return (r**0.5)
#functions
t=0#total
x=[]

for line in txt:
    t=t+1
    x.append(int(line))
s=my_sum(x)
a=int(s/t)#avarage
sd=my_st(x)#standard deviation

#code
print("total: ",t)
print("sum: ",s)
print("avarge: ",a)
print("standard deviation: ",sd)
