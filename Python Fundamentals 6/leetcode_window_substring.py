
s='ADOBECODEBANC'
t='ABC'
need={}
for c in t:
    need[c]=need.get(c,0)+1
left=0
missing=len(t)
start=0
size=float('inf')
for right,c in enumerate(s):
    if need.get(c,0)>0:
        missing-=1
    need[c]=need.get(c,0)-1
    while missing==0:
        if right-left+1<size:
            start=left
            size=right-left+1
        need[s[left]]=need.get(s[left],0)+1
        if need[s[left]]>0:
            missing+=1
        left+=1
result='' if size==float('inf') else s[start:start+size]
print("Minimum window:",repr(result))
