while True:
    n=int(input())
    if n==1:
        c=float(input())
        print("Celsius to Fahrenheit:",round(c*9/5+32,2))
    elif n==2:
        k=float(input())
        print("Kilometres to Miles:",round(k*0.621371,2))
    elif n==3:
        kg=float(input())
        print("Kilograms to Pounds:",round(kg*2.20462,2))
    elif n==4:
        print("Exit")
        break
    else:
        print("Invalid choice")
        continue