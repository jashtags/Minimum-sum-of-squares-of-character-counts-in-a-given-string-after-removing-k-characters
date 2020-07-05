import math
string=list(input())
s2=sorted(string,key=string.count)
k=int(input())
s2=s2[:-k]
ans=0
print(s2)
for i in set(s2):
    freq=s2.count(i)
    ans+=math.pow(freq,2)
    #ans+=s2.count(math.pow(i,2))
print(int(ans))
