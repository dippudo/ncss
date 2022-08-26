def sale_price(original, discount):
  # Calculate the sale price here.
  original = float(original)
  discount = float(discount)
  
  sale = float((1 - discount / 100) * original)
  number = round(sale,2)
  return number

# Write the rest of your program here
name = input("Product: ")
original_price = input("Original price ($): ")
discount = input("Discount (%): ")

print(f"{name} on sale for ${sale_price(original_price,discount)}.")
