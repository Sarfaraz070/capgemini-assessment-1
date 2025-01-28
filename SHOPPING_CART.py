
def calculate_total(items, prices):
    total_cost = sum(prices)
    return f"The total price of all the items is {total_cost}"

item_list = []
price_list = []

while True:
    item_name = input("Enter the item you want to buy: ")
    item_price = float(input("Enter the price of the item: "))
    item_list.append(item_name)
    price_list.append(item_price)
    
    more_items = input("Do you have more items to buy? (yes/no): ").strip().lower()
    if more_items != "yes":
        break

print("\nYour Shopping Cart:")
for index in range(len(item_list)):
    print(f"Item: {item_list[index]}, Price: {price_list[index]}")

print(calculate_total(item_list, price_list))