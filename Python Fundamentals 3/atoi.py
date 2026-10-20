s=input()
i=0
n=len(s)
while i<n and s[i].isspace():
 i+=1
sign=1
if i<n and s[i] in "+-":
 if s[i]=="-":
  sign=-1
 i+=1
num=0
found=False
while i<n and s[i].isdigit():
 num=num*10+ord(s[i])-ord("0")
 found=True
 i+=1
print(sign*num if found else 0)