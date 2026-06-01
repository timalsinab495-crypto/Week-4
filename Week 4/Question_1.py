# Question 1 — Small Shop Billing and Inventory System
# ============================================================
 
inventory = {
    "rice":  {"price": 120, "stock": 20},
    "milk":  {"price": 90,  "stock": 10},
    "bread": {"price": 60,  "stock": 15},
    "eggs":  {"price": 15,  "stock": 30}
}
 
cart = {
    "rice": 2,
    "milk": 3,
    "eggs": 12
}
 
def process_order(inventory, cart):
    bill = {}
    grand_total = 0
 
    for item, quantity in cart.items():
        if item not in inventory:
            print(f"Sorry, {item} is not available in the shop.")
            continue
 
        if inventory[item]["stock"] < quantity:
            print(f"Sorry, not enough stock for {item}")
            continue
 
        item_total = inventory[item]["price"] * quantity
        bill[item] = (quantity, item_total)
        grand_total += item_total
        inventory[item]["stock"] -= quantity
 
    print("\n---- Bill ----")
    for item, (qty, total) in bill.items():
        print(f"{item} x{qty} = NPR {total}")
    print(f"Grand Total: NPR {grand_total}")
    print("--------------")
 
    stock_info = ", ".join(f"{item}={info['stock']}" for item, info in inventory.items())
    print(f"Updated stock: {stock_info}")
 
process_order(inventory, cart)
 
