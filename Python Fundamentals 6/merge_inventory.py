
store_a={'LED':20,'Cable':10,'Board':3}
store_b={'Cable':5,'Sensor':7,'LED':8}
result=store_a.copy()
for item,qty in store_b.items():
    result[item]=result.get(item,0)+qty
print("Combined inventory:",result)
