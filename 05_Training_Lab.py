length = float(input())
width = float(input())

corridor = 100

places_l = length * 100 // 120
places_w = ((width * 100) - corridor) // 70
total_places = (places_l * places_w) - 3
print(f"{(total_places)}")