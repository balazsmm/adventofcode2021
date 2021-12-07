with open("2021_day7_input.txt", "r", encoding="utf-8") as ifile:
	positions = list(map(int, ifile.read().strip().split(",")))

def cumulative_consumption(distance): return int(distance * (distance + 1) / 2)

def min_pos_consumption(positions, cons_function):
	cons_dict = {guess: sum(cons_function(abs(elem-guess)) for elem in positions) for guess in range(min(positions), max(positions)+1)}
	min_fuel = min(cons_dict.values())
	min_value = [f for f in cons_dict if cons_dict[f] == min_fuel][0]
	return  min_fuel, min_value

print("Part 1: Min fuel {}, position for min fuel {}".format(*min_pos_consumption(positions, int)))
print("Part 2: Min fuel {}, position for min fuel {}".format(*min_pos_consumption(positions, cumulative_consumption)))
