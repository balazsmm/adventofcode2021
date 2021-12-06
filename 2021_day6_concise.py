with open("2021_day6_input.txt", "r", encoding="utf-8") as ifile:
	livestock = list(map(int, ifile.read().split(",")))

def cycle(initial, cycles):
	old_timers = {val: initial.count(val) for val in set(initial)}
	end_stock = cycle_timers(cycles, old_timers)
	print("Nr of lanternfish after {} cycles: {}".format(cycles, sum(end_stock[val] for val in end_stock)))
	
def cycle_timers(cycles_recvd, old_timers):
	for cycles in range(cycles_recvd - 1):
		new_timers = {timer_value - 1: old_timers.get(timer_value, 0) for timer_value in range(1, 9)}
		new_timers[8], new_timers[6] = (newbreed := old_timers.get(0,0)), new_timers.get(6, 0) + newbreed
		old_timers = new_timers
	return old_timers

lf = cycle(livestock, 80)
lf = cycle(livestock, 256)
