def calculate_bill(prices,tax_rate=0.10,discount=0.20):
    s=sum(prices)
    d=s*discount
    t=(s-d)*tax_rate
    print("Subtotal: %.2f"%s)
    print("Discount: %.2f"%d)
    print("Tax: %.2f"%t)
    print("Final total: %.2f"%(s-d+t))
calculate_bill([100,50],tax_rate=0.10,discount=0.20)