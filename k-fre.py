from collections import Counter
def top_k_frequent_logs(logs,k):
    tags=[]
    for log in logs:
        if ":" in log:
            tags.append(log.split(":")[0].strip())
    counts=Counter(tags)
    result=sorted(counts,key=lambda x:(-counts[x],x))
    return result[:k]
logs=["ERROR: db timeout","INFO: user login","ERROR: auth failed","WARNING: disk low","ERROR: lost connection","INFO: user logout"]
print(top_k_frequent_logs(logs,k=2))