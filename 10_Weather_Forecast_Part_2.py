temp = float(input())
result = ""
if 26.00 <= temp <= 35.00:
    result = "Hot"
elif 20.01 <= temp <= 25.9:
    result = "Warm"
elif 15.00 <= temp <= 20.00:
    result = "Mild"
elif 12.00 <= temp <= 14.9:
    result = "Cool"
elif 5.00 <= temp <= 11.9:
    result = "Cold"
else:
    result = "unknown"

print(result)