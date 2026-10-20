count=0
while True:
    n=int(input())
    if n<1 or n>100:
        print("Invalid input")
        count+=1
        continue
    print("Accepted value:",n)
    print("Invalid attempts:",count)
    break