
products=[("Sensor",4,150.0),("Cable",12,25.0),("Board",3,800.0)]
total=0
low=[]
for name,qty,price in products:
    value=qty*price
    total+=value
    print(f"{name}: Value = {value:.2f}")
    if qty<5:
        low.append(name)
print("Low-stock products:",low)
print(f"Total inventory value: {total:.2f}")
