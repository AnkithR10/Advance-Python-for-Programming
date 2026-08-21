'''Lambda'''
#Online Store Wants to calculate the Discounted Price of the Product
price = int(input("Enter Product Price:"))
dis = int(input("Ente rhe Discount:"))

final_price = lambda p,d:p-(p*d/100)
print("Final price:₹",final_price(price,dis))