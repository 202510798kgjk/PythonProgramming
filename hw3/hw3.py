import x_discount as xd

discount_rate=int(input("Discount rate: "))

a_discounted_price=int(input("What is the discounted price of product A? "))
b_discounted_price=int(input("What is the discounted price of product B? "))

print("The regular price of product A is {} won".format(xd.fixed_price(a_discounted_price,discount_rate)))
print("The regular price of product B is {} won".format(xd.fixed_price(b_discounted_price,discount_rate)))