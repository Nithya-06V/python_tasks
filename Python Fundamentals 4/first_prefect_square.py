l,r=map(int,input().split())
found=False
for i in range(max(0,l),r+1):
    j=0
    while j*j<i:
        j+=1
    if j*j==i:
        print("First perfect square:",i)
        found=True
        break
if not found:
    print("No perfect square found")