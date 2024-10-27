volume = int(input())
debit_1 = int(input())
debit_2 = int(input())
hours_gone = float(input())

debit_1_total = debit_1 * hours_gone
debit_2_total = debit_2 * hours_gone

volume_filled = (debit_1_total + debit_2_total)

debit_1_percentage = (debit_1_total / volume_filled) * 100
debit_2_percentage = (debit_2_total / volume_filled) * 100

volume_filled_percentage = (volume_filled / volume) * 100
volume_diff = volume_filled - volume

if volume_filled <= volume:
    print(f"The pool is {volume_filled_percentage :.2f}% full. Pipe 1: {debit_1_percentage :.2f}%. Pipe 2: {debit_2_percentage :.2f}%.")
else:
    print(f"For {hours_gone} hours the pool overflows with {volume_diff :.2f} liters.")
