m1=float(input("Enter mark 1: "))
m2=float(input("Enter mark 2: "))
m3=float(input("Enter mark 3: "))
avg=(m1+m2+m3)/3
print("Average:",avg)
if avg>=90:
    print("Grade A+")
elif avg>=75:
    print("Grade A")
elif avg>=50:
    print("Grade B")
else:
    print("Fail")