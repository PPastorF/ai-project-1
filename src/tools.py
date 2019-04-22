from math import sqrt
from ast import literal_eval

# calculo da heurisitca para um no
def euclidian_distance(node_a, node_b):
	a = literal_eval(node_a)
	b = literal_eval(node_b)

	hor = abs(b[0] - a[0])
	ver = abs(b[1] - a[1])

	return sqrt(hor**2 + ver**2)