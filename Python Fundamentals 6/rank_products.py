
sales={'Sensor':[4,6,5],'Cable':[10,2,3],'Board':[8,7],'LED':[5,5,5]}
result=sorted(sales.items(),key=lambda x:(-sum(x[1]),x[0]))
for product,values in result:
    print(f"{product}: {sum(values)}")
