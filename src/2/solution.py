def productOf(ints):
	import math
	return list(map(lambda i : math.prod(ints) // i, ints))

def withoutDivision(ints):
	import math
	r = []
	for q in range(len(ints)):
		n = ints * 1
		del n[q]
		r.append(math.prod(n))
	return r
