a=[2,5,8,11,15,17,20,23]
for i in a:
    if i>1:
        count=0
        for j in range(2,i):
            if i%j==0:
                count=count+1
        if count==0:
            print(i)