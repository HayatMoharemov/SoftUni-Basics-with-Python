skumriq_price_per_kg = float(input())
caca_price_per_kg = float(input())
palamud_kg = float(input())
safrid_kg = float(input())
midi_kg = int(input())

midi_price = 7.50 * midi_kg # 7.50
palamud_per_kg = skumriq_price_per_kg * 1.6
safrid_per_kg = caca_price_per_kg * 1.8

palamud_price = palamud_per_kg * palamud_kg
safrid_price = safrid_per_kg * safrid_kg

sum = midi_price + palamud_price +safrid_price
print(f"{sum :.2f}")



# Числото трябва да е форматирано до вторият знак след десетичната запетая