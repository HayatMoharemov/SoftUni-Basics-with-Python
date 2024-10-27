holidays = int(input())

year = 365
playtime_yearly = 30_000
playtime_working_minutes = 63
playtime_holiday_minutes = 127

play_time_holiday = playtime_holiday_minutes * holidays
play_time_working = (year - holidays) * playtime_working_minutes
total_playtime = play_time_holiday + play_time_working

time_left = playtime_yearly - total_playtime
time_left = abs(time_left)
total_playtime_minutes = time_left % 60
total_playtime_hours = time_left // 60

if total_playtime <= playtime_yearly:
    print("Tom sleeps well")
    print(f"{total_playtime_hours} hours and {total_playtime_minutes} minutes less for play")
else:
    print("Tom will run away")
    print(f"{total_playtime_hours} hours and {total_playtime_minutes} minutes more for play")

