'''
Projeto 1 - Inteligencia Artificial
Professor Alneu de Andrade Lopes

Pedro Pastorello Fernandes - NUSP 10262602
Vinicius Leite Ribeiro - NUSP 10388200
Luiz Guilherme Martins - NUSP 10392171
'''

from math import sqrt
from ast import literal_eval

# calculo da heurisitca para um no
def heuristic_calc(node_a, node_b):
	return euclidian_distance(node_a, node_b)

# heuristica de distancia em linha reta
def euclidian_distance(node_a, node_b):
	a = literal_eval(node_a)
	b = literal_eval(node_b)

	hor = abs(b[0] - a[0])
	ver = abs(b[1] - a[1])

	return sqrt(hor**2 + ver**2)

# heuristica de distancia da soma dos catetos
def leg_distance(node_a, node_b):
	a = literal_eval(node_a)
	b = literal_eval(node_b)

	hor = abs(b[0] - a[0])
	ver = abs(b[1] - a[1])

	return hor + ver