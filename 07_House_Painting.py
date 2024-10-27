#razhod zelena boq = 1 l / 3.4 m2
#razhod chervena boq = 1 l / 4.3 m2

# 1.	x – височината на къщата – реално число в интервала [2...100]
# 2.	y – дължината на страничната стена – реално число в интервала [2...100]
# 3.	h – височината на триъгълната стена на прокрива – реално число в интервала [2...100]

height = float(input())
length = float(input())
height_ceiling = float(input())

window = 1.5 * 1.5
door = 1.2 * 2
front_wall = height * height # 36
side_wall = height * length # 60
ceiling_1 = 2 * (height * length)
ceiling_2 = 2 * ((height * height_ceiling) / 2)
ceiling = ceiling_1 + ceiling_2

total_house = (front_wall*2 + side_wall*2) - (window * 2 + door)

green_paint = total_house / 3.4
red_paint = ceiling / 4.3

print(f"{green_paint :.2f}")
print(f"{red_paint :.2f}")