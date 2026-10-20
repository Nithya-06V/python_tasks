n=int(input())
s=input().strip()
best=s[0]
length=1
value=s[0]
count=1
for i in range(1,len(s)):
    if s[i]==s[i-1]:
        count+=1
    else:
        count=1
    if count>length:
        length=count
        best=s[i]
print("Value =",best)
print("Length =",length)