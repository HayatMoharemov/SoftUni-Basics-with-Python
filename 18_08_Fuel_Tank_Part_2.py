fuel_type = input()
fuel_qty = float(input())
discount_card = input()

gasoline_price = 2.22
gas_price = 0.93
diesel_price = 2.33
fuel_price = 0.0
discount_per_liter = 0.0

if fuel_type == "Gas" and discount_card == "Yes":
    discount_per_liter = 0.08 * fuel_qty
    fuel_price = gas_price
elif fuel_type == "Gas" and discount_card == "No":
    fuel_price = gas_price
elif fuel_type == "Gasoline" and discount_card == "Yes":
    discount_per_liter = 0.18 * fuel_qty
    fuel_price = gasoline_price
elif fuel_type == "Gasoline" and discount_card == "No":
    fuel_price = gasoline_price
elif fuel_type == "Diesel" and discount_card == "Yes":
    discount_per_liter = 0.12 * fuel_qty
    fuel_price = diesel_price
elif fuel_type == "Diesel" and discount_card == "No":
    fuel_price = diesel_price

total_price = (fuel_price * fuel_qty) - discount_per_liter

if 20 <= fuel_qty <= 25:
    total_price = total_price - (total_price * 0.08)
elif fuel_qty > 25:
    total_price = total_price - (total_price * 0.10)

print(f"{total_price :.2f} lv.")
