stock_items = [15, 4, 20, 3, 12, 2]
total_items= 0

for item in stock_items :
    total_items += item
    if item <5:
        print (f"Restock needed: only [{item}] left")

print (f"Total items in stock: [{total_items}]")
    