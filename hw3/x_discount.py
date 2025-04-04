def fixed_price(price,discount_rate=100):
    if price <=0:
        print("price value is invaild: it is set to default value of 1000")
        price=1000
    return price*(1/(1-discount_rate/100))