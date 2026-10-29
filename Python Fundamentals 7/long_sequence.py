def longest_consecutive(nums):
    s=set(nums)
    m=0
    for n in s:
        if n-1 not in s:
            c=1
            while n+c in s:
                c+=1
            m=max(m,c)
    return m
nums=[100,4,200,1,3,2]
print("Longest consecutive sequence length:",longest_consecutive(nums))
print("Sequence: 1, 2, 3, 4")