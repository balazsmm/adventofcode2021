with open("2021_day5_input.txt", "r", encoding="utf-8") as ifile:
	vectors = [(list(map(int,(z := if_line.split(" -> "))[0].split(","))), list(map(int,z[1].strip().split(","))) ) for if_line in ifile.readlines()]
	
print(vectors)

def is_straight(origin, destination):
		return not all(origin[crd] != destination[crd] for crd in (0,1))

class FieldMap:
	def __init__(self, vectors):
		self.vectors = vectors
		self.coordinates = {}
		self.draw_all_vectors()
		
	def calculate_max_and_mins(self):
		datasets = dict()
		
		for count, val in enumerate(["x", "y"]):
			datasets[val]= [elem for ln in [[line[0][count], line[1][count]] for line in self.vectors] for elem in ln]
			print("{}: min: {}, max: {}".format(val, min(datasets[val]), max(datasets[val])))
			
	def draw_straight_line(self, vector):
		coords = dict()
		if is_straight(*vector):
			coords[0], coords[1] = [c[0] for c in vector], [c[1] for c in vector]
			for ch_coord in (0,1):
				coords[str(ch_coord) + "values"] = list(range(min(coords[ch_coord]),max(coords[ch_coord])+1))
		
			for first in coords["0values"]:
				for second in coords['1values']:
					self.increment_coordinate(first, second)
		else:
			self.draw_any_line(vector)
	
	def draw_any_line(self, vector):
		coords = dict()
		coords[0], coords[1] = [c[0] for c in vector], [c[1] for c in vector]
		for ch_coord in (0, 1):
			coords[str(ch_coord) + "increment"] = 1 if coords[ch_coord][1] > coords[ch_coord][0] else -1
			coords[str(ch_coord) + "values"] = list(range(coords[ch_coord][0], coords[ch_coord][1]+coords[str(ch_coord) + "increment"], coords[str(ch_coord) + "increment"]))
		
		for coord_tuple in zip(coords["0values"], coords["1values"]):
			self.increment_coordinate(*coord_tuple)
	
		
	def increment_coordinate(self, first, second):
		if (first, second, ) not in self.coordinates:
			self.coordinates[(first, second, )] = 1
		else:
			self.coordinates[(first, second, )] += 1
	
	def draw_all_vectors(self):
		for vector in self.vectors:
			self.draw_straight_line(vector)
			
	def count_overlaps(self, threshold=None):
		if not threshold:
			threshold = 2
		return sum(1 for ch_cord in self.coordinates if self.coordinates[ch_cord]>=threshold)
	
f_m = FieldMap(vectors)
print("Overlaps: {}".format(f_m.count_overlaps()))