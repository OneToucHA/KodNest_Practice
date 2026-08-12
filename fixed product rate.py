# Read input values
product_id = input()
product_name = input()
category = input()
unit_price = float(input())
quantity = int(input())
reorder_level = int(input())

# Store in a tuple (must NOT contain reorder_level)
product_record = (product_id, product_name, category, unit_price, quantity)

# Access using tuple indexing
indexed_product_id = product_record[0]
indexed_product_name = product_record[1]

# Unpack tuple into separate variables
p_id, p_name, p_category, p_price, p_quantity = product_record

# Calculate total stock value
stock_value = p_price * p_quantity

# Determine stock status
if p_quantity == 0:
    stock_status = "Out of Stock"
elif p_quantity <= reorder_level:
    stock_status = "Reorder Required"
else:
    stock_status = "Sufficient Stock"

# Display processed product record
print(f"Product ID: {indexed_product_id}")
print(f"Product Name: {indexed_product_name}")
print(f"Category: {p_category}")
print(f"Unit Price: {p_price:.2f}")
print(f"Available Quantity: {p_quantity}")
print(f"Stock Value: {stock_value:.2f}")
print(f"Stock Status: {stock_status}")