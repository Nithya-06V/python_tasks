n=int(input())
skip=0
for i in range(1,21):
    r=n*i
    if r>100:
        break
    if r%3==0:
        skip+=1
        continue
    print(f"{n}x{i}={r}")
print("Skipped results:",skip)