with open("2021_day2_input.txt", "r", encoding="utf-8") as inst_file:
	instructions = [inst_line.strip().split(" ") for inst_line in inst_file.readlines()]

forward = sum(int(il[1]) if il[0] == "forward" else 0 for il in instructions)
depth = sum(0 if il[0] == "forward" else (int(il[1]) if il[0] == "down" else -int(il[1])) for il in instructions)

print("Horizontal: {}, depth: {}, multiplied: {}".format(forward, depth, forward*depth))

depth, forward, aim = 0, 0, 0

for il in instructions:
	inst_val = int(il[1])
	match il[0]:
		case "up":
			aim -= inst_val
		case "down":
			aim += inst_val
		case "forward":
			forward += inst_val
			depth += inst_val*aim

print("2nd: Horizontal: {}, depth: {}, multiplied: {}".format(forward, depth, forward*depth))