n=int(input("N: "))
a=int(input("Divisor 1: "))
w1=input("Word 1: ")
b=int(input("Divisor 2: "))
w2=input("Word 2: ")
for i in range(1,n+1):
 if i%a==0 and i%b==0:
  print(w1+w2)
 elif i%a==0:
  print(w1)
 elif i%b==0:
  print(w2)
 else:
  print(i)