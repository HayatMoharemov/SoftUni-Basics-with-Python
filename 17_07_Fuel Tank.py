fuel_type = input()
litres = float(input())

if fuel_type == "Diesel" and litres >= 25 \
        or fuel_type == "Gasoline" and litres >= 25 \
        or fuel_type == "Gas" and litres >= 25:
    print(f"You have enough {str.lower(fuel_type)}.")
elif fuel_type == "Diesel" and litres < 25 \
        or fuel_type == "Gasoline" and litres < 25 \
        or fuel_type == "Gas" and litres < 25:
    print(f"Fill your tank with {str.lower(fuel_type)}!")
else:
    print("Invalid fuel!")
