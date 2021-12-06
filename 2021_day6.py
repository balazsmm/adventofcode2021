with open("2021_day6_input.txt", "r", encoding="utf-8") as ifile:
	livestock = list(map(int, ifile.read().split(",")))
	

class Cycle:
	def __init__(self, initial, cycles):
		self.cycles = cycles
		self.old_timers = {val: initial.count(val) for val in set(initial)}
		self.cycle_timers()
		print("Nr of lanternfish after {} cycles: {}".format(self.cycles, sum(self.old_timers[val] for val in self.old_timers)))
	
	def cycle_timers(self):
		for cycles in range(self.cycles-1):
			new_timers = {timer_value-1: self.old_timers.get(timer_value, 0) for timer_value in range(1, 9)}
			if 0 in self.old_timers:
				new_timers[8] = (newly_bred := self.old_timers[0])
				new_timers[6] = new_timers.get(6, 0)+newly_bred
			self.old_timers = new_timers


lf = Cycle(livestock, 80)
lf = Cycle(livestock, 256)
