import operator
li=set()
g={}
def most_frequent(str):
    c=list(str)
    for i in range(0,len(str)):
        d=str.count(c[i])
        if(d>=1):
            g[c[i]]=d    
    for i in range(0,len(str)):
        d=str.count(c[i])       
        if d>=2:
            li.add(c[i])
            
    
def pr():
    f=dict( sorted(g.items(), key=operator.itemgetter(1),reverse=True))
    print(f)
    print("the frequency of the each elements are :")
    for w in f:
        print(w,"=",f[w])

i=input("Enter the name of which you find the repetation :")
most_frequent(i)
print("the repeated alpha bets in the passage are : ",end="")
print(li)
print("frequency of the alphabets are :")
print(g)
print("The sorted list in the descending order is :")
pr()
