distance = int(input())
time_of_the_day = input()

taxi_start = 0.70
taxi_day = 0.79
taxi_night = 0.90
bus = 0.09
train = 0.06
result = ""
if time_of_the_day == "day" and distance < 20:
    result = taxi_start + (taxi_day * distance)
elif time_of_the_day == "night" and distance < 20:
    result = taxi_start + (taxi_night * distance)
elif 20 <= distance < 100:
    result = bus * distance
elif distance >= 100:
    result = train * distance

print(f"{result :.2f}")


