import math
days = int(input())
total_food = int(input()) #kg
dog_food = float(input()) #kg
cat_food = float(input()) #kg
tortoise_food = float(input()) #grams

dog_food_needed = dog_food * days
cat_food_needed = cat_food * days
tortoise_food_needed = (tortoise_food * days) / 1000

total_consumed_food = dog_food_needed + cat_food_needed + tortoise_food_needed

if total_food >= total_consumed_food:
    food_diff = total_food - total_consumed_food
    print(f"{math.floor(food_diff)} kilos of food left.")
else:
    food_diff = total_consumed_food - total_food
    print(f"{math.ceil(food_diff)} more kilos of food are needed.")