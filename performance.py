def analyze_students(records):
    qualified=[]
    topper=""
    highest=0
    for name,m1,m2,m3 in records:
        total=m1+m2+m3
        average=total/3
        if average>=75:
            qualified.append(name)
        if total>highest:
            highest=total
            topper=name
    return {"qualified":qualified,"topper":topper}

records=[("Asha",85,78,92),("Bala",65,72,70),("Charan",90,88,95),("Divya",76,80,74),("Esha",60,68,72)]
print(analyze_students(records))