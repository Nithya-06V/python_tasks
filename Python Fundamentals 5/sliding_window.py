
sales=[10,20,30,40,50,60]
k=3
result=[]
for i in range(len(sales)-k+1):
    avg=sum(sales[i:i+k])/k
    result.append(f"{avg:.2f}")
print("Window averages:", "["+", ".join(result)+"]")
