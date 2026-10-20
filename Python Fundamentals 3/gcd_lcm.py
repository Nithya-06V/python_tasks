a=int(input("Number 1: "))
b=int(input("Number 2: "))
def convert(n,base):
 d="0123456789ABCDEF"
 s=""
 while n>0:
  s=d[n%base]+s
  n//=base
 return s or "0"
x,y=a,b
while y:
 x,y=y,x%y
g=x
print("Binary        :",convert(a,2))
print("Octal        :",convert(a,8))
print("Hexadecimal :",convert(a,16))
print("GCD          :",g)
print("LCM          :",a*b//g)