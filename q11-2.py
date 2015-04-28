t=open("banana.txt","r")
#function:
def find_banana(t):
    b=0
    for line in t:
        x=line.lower()
        if(x.find('banana')==0):
            b=b+1
    return(b)

#code
ban=find_banana(t)
print("in this text there are ",ban,"bananas")
