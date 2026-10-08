data=[" Asha, Chennai, 25 ","Bala, chennai, 30"," asha, Chennai, 25","Charan, Bangalore, 28","Bala, Chennai, 30 "]
result=[]
for record in data:
    name,city,age=record.strip().split(",")
    name=name.strip().title()
    city=city.strip().title()
    age=int(age.strip())
    customer={"name":name,"city":city,"age":age}
    if customer not in result:
        result.append(customer)
print(result)