import  math

area = int(input())
grapes_per_sqm = float(input())
wine_needed = int(input())
workers = int(input())
grapes_per_liter_wine = 2.5

total_grapes = area * grapes_per_sqm
grapes_for_wine = total_grapes * 0.4
wine_produced = grapes_for_wine / 2.5
wine_diff = wine_produced - wine_needed
wine_diff = abs(wine_diff)
wine_per_worker = wine_diff / workers

if wine_produced < wine_needed:
    print(f"It will be a tough winter! More {math.floor(wine_diff)} liters wine needed.")
else:
    print(f"Good harvest this year! Total wine: {math.floor(wine_produced)} liters.")
    print(f"{math.ceil(wine_diff)} liters left -> {math.ceil(wine_per_worker)} liters per person.")