with open("2021_day4_input.txt", "r", encoding="utf-8") as ifile:
	raw_input_data = ifile.readlines()
drawn_numbers = raw_input_data.pop(0).split(",")
tables = [[raw_input_data[slc_start + ln_nr].split() for ln_nr in range(1, 6)] for slc_start in range(0, len(raw_input_data), 6)]


def full_line_match(table, lot):
	for line in table:
		if all(elem in lot for elem in line):
			return True


def full_column_match(table, lot):
	for column_number in range(len(table[0])):
		if all(line[column_number] in lot for line in table):
			return True


def check_all_bingos(drawn_numbers, tables, firstmatch=None):
	last_drawn_lot, last_checked_table = [], []
	bingo_tables, table_count = [], len(tables)
	for draw_lot_range in range(1, len(drawn_numbers)):
		drawn_lot = drawn_numbers[:draw_lot_range]
		for checked_table in tables:
			if full_line_match(checked_table, drawn_lot) or full_column_match(checked_table, drawn_lot):
				if firstmatch:
					return drawn_lot, checked_table
				if checked_table not in bingo_tables:
					bingo_tables.append(checked_table)
					last_drawn_lot, last_checked_table = drawn_lot, checked_table
				if len(bingo_tables) == table_count:
					return last_drawn_lot, last_checked_table


def score(lot, tbl):
	return sum(int(element) for line in tbl for element in line if element not in lot)*int(lot[-1])


lot1, tbl1 = check_all_bingos(drawn_numbers, tables, firstmatch=True)
lot2, tbl2 = check_all_bingos(drawn_numbers, tables)

print("Part 1 score: {}, Part 2 score: {}".format(score(lot1, tbl1), score(lot2, tbl2)))
