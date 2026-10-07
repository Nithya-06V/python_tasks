n=int(input("Enter number: "))
x=n
rev=0
while n>0:
    r=n%10
    rev=rev*10+r
    n=n//10
print("Reverse:",rev)
if x==rev:
    print("Palindrome")
else:
    print("Not a Palindrome")