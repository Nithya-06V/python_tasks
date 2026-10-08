numbers=[10,20,10,30,20,40,30,50]
result=[]
for number in numbers:
    if number not in result:
        result.append(number)
print(result)