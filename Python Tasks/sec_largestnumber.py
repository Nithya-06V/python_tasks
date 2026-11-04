a=[10,25,5,40,15]
large=a[0]
second=None
for i in a:
    if i>large:
        second=large
        large=i
    elif i<large:
        if second==None or i>second:
            second=i
print("Second largest number:",second)