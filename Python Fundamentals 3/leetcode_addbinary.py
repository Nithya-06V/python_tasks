a=input("a = ")
b=input("b = ")
i=len(a)-1
j=len(b)-1
c=0
s=""
while i>=0 or j>=0 or c:
 x=int(a[i]) if i>=0 else 0
 y=int(b[j]) if j>=0 else 0
 t=x+y+c
 s=str(t%2)+s
 c=t//2
 i-=1
 j-=1
print(s)