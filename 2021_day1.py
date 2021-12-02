with open("2021_day1_input.txt", "r", encoding="utf-8") as ifile:
	readings = [int(i) for i in ifile.readlines()]
increases = sum(1 for i in range(1, len(readings)) if readings[i]> readings[i-1])
three_measurement_window_increases = sum(1 for i in range(4, len(readings)+1) if sum(readings[i-3:i])> sum(readings[i-4:i-1]))
print("Larger measurements than the previous: {} (single), {} (three element window)".format(increases, three_measurement_window_increases))