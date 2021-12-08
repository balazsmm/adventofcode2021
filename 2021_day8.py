from functools import reduce

with open("2021_day8_input.txt", "r", encoding="utf-8") as ifile:
	input_lists = [list(map(str.split, io_list.strip().split(" | "))) for io_list in ifile.readlines()]

letter_sets = [	("0", set("abcefg")), ("1", set("cf")), ("2", set("acdeg")), ("3", set("acdfg")),  ("4", set("bcdf")), ("5", set("abdfg")), ("6", set("abdefg")), ("7", set("acf")), ("8", set("abcdefg")), ("9", set("abcdfg"))]


def sort_by_length(code_list):
	ln_dict = {i: [elem for elem in code_list if len(elem) == i] for i in range(2, 8)}
	for i in (2, 3, 4, 7):
		ln_dict[i] = ln_dict[i][0]
	return ln_dict


def get_code_pairs(codeword_lengths):
	code_pairs = dict()
	code_pairs[(a := (set(codeword_lengths[3]) - set(codeword_lengths[2])).pop())] = "a"
	b_d = set(codeword_lengths[4]) - set(codeword_lengths[2])
	code_pairs[(d := (reduce(set.intersection, [set(pc) for pc in codeword_lengths[5]]+[b_d])).pop())] = "d"
	code_pairs[(b := (b_d - set(d)).pop())] = "b"
	zero = [seq for seq in codeword_lengths[6] if d not in seq][0]
	codeword_lengths[6].remove(zero)
	nr_six = [seq for seq in codeword_lengths[6] if any([lr not in seq for lr in codeword_lengths[2]])][0]
	codeword_lengths[6].remove(nr_six)
	nr_nine = codeword_lengths[6].pop()
	for letter in codeword_lengths[2]:
		if letter in nr_six:
			code_pairs[(f := letter)] = "f"
		else:
			code_pairs[(c := letter)] = "c"
	code_pairs[(e := (set(codeword_lengths[7]) - set(nr_nine)).pop())] = "e"
	code_pairs[(set(codeword_lengths[7]) - set((a, b, c, d, e, f))).pop()] = "g"
	return code_pairs


part1 = sum(1 for lst in [e[1] for e in input_lists] for cnt in lst if len(cnt) in {2, 4, 3, 7})

total_sum = 0
for line in input_lists:
	code_pairs = get_code_pairs(sort_by_length(line[0]))
	translated_value = [[code_pairs[digit] for digit in number] for number in line[1]]
	total_sum += int("".join([element[0] for elem in translated_value for element in letter_sets if element[1] == set(elem)]))

print("Part 1 - Unambigous values: {} Part 2- Grand total: {}".format(part1, total_sum))
