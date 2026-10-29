def top_k_frequent(nums,k):
    d={}
    for n in nums:
        d[n]=d.get(n,0)+1
    return sorted(d,key=lambda x:d[x],reverse=True)[:k]
nums=[1,1,1,2,2,3]
print("Top 2 frequent values:",top_k_frequent(nums,2))