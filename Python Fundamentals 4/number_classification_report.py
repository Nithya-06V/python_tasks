n=int(input())
a=list(map(int,input().split()))
p=neg=z=e=o=b=c=d=ne=0
for x in a:
    if x>0:
        p+=1
    elif x<0:
        neg+=1
    else:
        z+=1
    if x!=0:
        if x%2==0:
            e+=1
        else:
            o+=1
    if x!=0:
        if x%3==0 and x%5==0:
            b+=1
        elif x%3==0:
            c+=1
        elif x%5==0:
            d+=1
        else:
            ne+=1
print("Positive:",p)
print("Negative:",neg)
print("Zero:",z)
print("Even:",e)
print("Odd:",o)
print("Divisible by both 3 and 5:",b)
print("Divisible only by 3:",c)
print("Divisible only by 5:",d)
print("Divisible by neither:",ne)