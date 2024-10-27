price_per_kg_veg = float(input())
price_per_kg_fru = float(input())
sum_kg_veg = int(input())
sum_kg_fru = int(input())

sum_euro = ((price_per_kg_veg * sum_kg_veg) + (price_per_kg_fru * sum_kg_fru)) / 1.94

print(f"{sum_euro :.2f}")