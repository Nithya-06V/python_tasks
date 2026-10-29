def find_max_length(nums):
    d={0:-1}
    b=0
    m=0
    for i,n in enumerate(nums):
        b+=1 if n==1 else -1
        if b in d:
            m=max(m,i-d[b])
        else:
            d[b]=i
    return m
print("Maximum balanced subarray length:",find_max_length([0,1,0]))