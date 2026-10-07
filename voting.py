age=int(input("Enter age: "))
vote="Eligible" if age>=18 else "Not Eligible"
discount="Eligible" if age>=60 else "Not Eligible"
print("Voting:",vote)
print("Senior Citizen Discount:",discount)