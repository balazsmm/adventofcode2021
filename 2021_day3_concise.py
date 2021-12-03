with open("2021_day3_input.txt", "r", encoding="utf-8") as ifile:
	inputs = [ln.strip() for ln in ifile.readlines()]

# Part 1
gamma_rate = int("".join(['1' if [lin[n] for lin in inputs].count('1') > len(inputs) / 2 else "0" for n in range(0, len(inputs[0]))]), 2)
delta_rate = int(bin(gamma_rate ^ 0b111111111111), 2)
print("Power consumption {}".format(gamma_rate * delta_rate))


# Part2
def common_criteria(stack, position, default):
	stack_len = len(stack)
	count_1 = [lin[position] for lin in stack].count("1")
	if count_1 == stack_len - count_1:
		return default
	elif (count_1 > stack_len - count_1 and default == "1") or (count_1 < stack_len - count_1 and default == "0"):
		return "1"
	return "0"


class Filterer:
	def __init__(self, stack, default_value):
		# reusable stack
		self.stack = list(stack)
		self.default_value = default_value
	
	def process_stack(self):
		for i in range(len(self.stack[0])):
			self.stack = self.filter_by_most_common(i)
			if len(self.stack) == 1:
				return self.stack[0]
	
	def filter_by_most_common(self, position):
		filter_criteria = common_criteria(self.stack, position, self.default_value)
		retval = [lin for lin in self.stack if lin[position] == filter_criteria]
		return retval


o2 = Filterer(inputs, '1')
o2_reading = int(o2.process_stack(), 2)
co2 = Filterer(inputs, '0')
co2readings = int(co2.process_stack(), 2)
print("Life support rating: {}".format(o2_reading * co2readings))
