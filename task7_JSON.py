import json
with open("data/products.json","r")as file:
  products=json.load(file)

print("{:<15} {:<15} {:<15}".format("Name", "Price","Quantity"))
print("-"*45)

for product in products:
  print("{:<15} {:<15} {:<15}".format(product["name"],product["price"],product["quantity"]))