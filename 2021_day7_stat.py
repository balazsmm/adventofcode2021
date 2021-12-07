from statistics import median, mean

with open("2021_day7_input.txt", "r", encoding="utf-8") as ifile:
	positions = list(map(int, ifile.read().strip().split(",")))

def cumulative_consumption(distance): return int(distance * (distance + 1) / 2)
def total_consumption(distance, positions, cons_function): return sum(cons_function(abs(elem-distance)) for elem in positions)

print("Part 1: Min fuel {}".format(total_consumption(int(median(positions)), positions, int)))
print("Part 2: Min fuel {}".format(total_consumption(int(mean(positions)), positions, cumulative_consumption)))
