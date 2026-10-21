
names=['Anu','Arun','Bala','Banu','Cathy','Asha']
result={}
for name in names:
    key=name[0].upper()
    result.setdefault(key,[]).append(name)
print(result)
