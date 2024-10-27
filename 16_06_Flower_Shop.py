import math
magnolia = int(input())
zyumbyul = int(input())
rose = int(input())
cactus = int(input())
present_price = float(input())

taxes = 0.05 # obshtata suma
magnoalia_price = 3.25
zyumbyul_price = 4.00
roses_price = 3.50
cactus_price = 8.00

total_sold = ((magnolia * magnoalia_price) + (zyumbyul * zyumbyul_price) + (rose * roses_price) + (cactus * cactus_price))
profit = total_sold - (total_sold * taxes)

if profit >= present_price:
    diff = profit - present_price
    print(f"She is left with {math.floor(diff)} leva.")
else:
    diff = present_price - profit
    print(f"She will have to borrow {math.ceil(diff)} leva.")
