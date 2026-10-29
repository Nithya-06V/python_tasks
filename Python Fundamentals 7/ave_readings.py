def average_readings(*args):
    if not args:
        return None
    return sum(args)/len(args)
a=average_readings(10,20,30,40)
print("Average:",a)
if average_readings() is None:
    print("No readings provided")