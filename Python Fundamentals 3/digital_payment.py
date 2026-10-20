n=int(input("Transactions: "))
a=[]
r=0
for i in range(n):
 try:
  x=float(input())
  if x<0:
   r+=1
  else:
   a.append(x)
 except ValueError:
  r+=1
print("Successful Transactions :",len(a))
print(f"Total Amount          : ₹{sum(a):.2f}")
if a:
 print(f"Highest Transaction     : ₹{max(a):.2f}")
 print(f"Lowest Transaction      : ₹{min(a):.2f}")
 print(f"Average Transaction      : ₹{sum(a)/len(a):.2f}")
else:
 print("No successful transactions")
print("Rejected Transactions :",r)