from math import prod

with open("2021_day9_input.txt", "r", encoding="utf-8") as ifile:
	h_map = [[int(point) for point in line.strip()] for line in ifile.readlines()]


class Slices:
	def __init__(self, heightmap):
		self.heightmap = heightmap
		self.east_range, self.south_range = range(len(heightmap[0])), range(len(heightmap))
		self.iterate_and_sum_elements()
		self.flowmap_flow()
	
	def checked_range(self, east, south):
		return [east_coord for east_coord in range(east-1, east+2) if east_coord in self.east_range], [south_coord for south_coord in range(south-1, south+2) if south_coord in self.south_range]
	
	def slice(self, east, south):
		checked_east, checked_south = self.checked_range(east, south)
		return [self.heightmap[line][elem] for line in checked_south for elem in checked_east]
	
	def iterate_and_sum_elements(self):
		self.sum_risk_levels = 0
		for ypos, ln in enumerate(self.heightmap):
			for xpos, pnt in enumerate(ln):
				if self.heightmap[ypos][xpos] == min(self.slice(xpos, ypos)):
					self.sum_risk_levels += self.heightmap[ypos][xpos]+1
		print("Sum of risk levels: {}".format(self.sum_risk_levels))
	
	def flowmap_flow(self):
		self.flowmap =[[0 if self.heightmap[ypos][xpos] == 9 else 1 for xpos, elem in enumerate(line)] for ypos, line in enumerate(self.heightmap)]
		for height_pos in range(8, -1, -1):
			for ypos, ln in enumerate(self.heightmap):
				for xpos, pnt in enumerate(ln):
					if self.heightmap[ypos][xpos] == height_pos:
						self.flow_position(xpos, ypos)

		product_of_top_three = prod(sorted([self.flowmap[ypos][xpos] for ypos, ln in enumerate(self.flowmap) for xpos, elem in enumerate(ln)])[-3:])
		print("Size of three largest basins multiplied: {}".format(product_of_top_three))

	def flow_position(self, east, south):
		if self.heightmap[south][east] == 0:
			return
		checked_east, checked_south = self.checked_range(east, south)
		for coord_pair in ((east-1, south), (east, south-1), (east+1, south), (east, south+1)):
			if coord_pair[0] in checked_east and coord_pair[1] in checked_south:
				if self.heightmap[south][east] > self.heightmap[coord_pair[1]][coord_pair[0]]:
					self.flowmap[coord_pair[1]][coord_pair[0]] += self.flowmap[south][east]
					self.flowmap[south][east] = 0
					return
				
				
if __name__ == "__main__":
	testdata = """2199943210
3987894921
9856789892
8767896789
9899965678"""
	# Test data
	Slices([[int(point) for point in line.strip()] for line in testdata.split("\n")])
	# Input data
	Slices(h_map)
	