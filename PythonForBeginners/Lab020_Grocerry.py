prices = {
    "apple" : 0.50,
    "banana" : 1.00,
    "milk" : 2.00,
    "bread" : 3.00,
    "orange" : 4.00,
    "cheese" : 5.00,
}

item1_name = input("enter the name of the first item :").lower()
item1_qty = int(input(f"enter the quantity of the first item {item1_name} "))

item2_name = input("enter the name of the second item :").lower()
item2_qty = int(input(f"enter the quantity of the second item {item2_name} "))

item3_name = input("enter the name of the third item :").lower()
item3_qty = int(input(f"enter the quantity of the third item {item3_name} "))

item1_price = prices.get(item1_name,1)
item2_price = prices.get(item2_name,1)
item3_price = prices.get(item3_name,1)

item1_total = item1_price * item1_qty
item2_total = item2_price * item2_qty
item3_total = item3_price * item3_qty

subtotal = item1_total + item2_total + item3_total
tax = subtotal * 0.085
total_amount = subtotal + tax

print("\n----Receipt----")
print(f"{item1_name.capitalize()} : {item1_qty} @ ${item1_price:.2f} each = ${item1_total:.2f}$")
print(f"{item2_name.capitalize()} : {item2_qty} @ ${item2_price:.2f} each = ${item2_total:.2f}$")
print(f"{item3_name.capitalize()} : {item3_qty} @ ${item3_price:.2f} each = ${item3_total:.2f}$")
print("\n----Total----")
print(f"SubTotal : ${subtotal:.2f}$")
print(f"Tax (8.5%): ${tax:.2f}$")
print(f"Total Amount : ${total_amount:.2f}$")
print("\n---------------")