def group_anagrams(strs):
    d={}
    for s in strs:
        k="".join(sorted(s))
        if k not in d:
            d[k]=[]
        d[k].append(s)
    return list(d.values())
for g in group_anagrams(["eat","tea","tan","ate","nat","bat"]):
    print(g)