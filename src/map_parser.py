from src.graph import Graph
from math import sqrt

# transforma uma string em uma lista
def line_to_list(line_string):
	return list( line_string.strip() )

# dado um arquivo de mapa, retorna uma matriz representando tal mapa
def read_filemap(file_path):

	with open(file_path, "r") as file:
		line = file.readline()			
		line = line.strip()
		dimensions = line.split(' ')

		arr = []
		while line:
			line = file.readline()
			if not line:
				break
			arr.append( line_to_list(line) )

	return arr

# dado uma matriz, retorna os indices adjacentes lado-a-lado de um indice
def side_adjacents(array, index):
	I = index[0]
	J = index[1]
	adj = []

	sides = [
		(I-1, J),
		(I, J-1),
		(I, J+1),
		(I+1, J)
	]

	for index in sides:
		i = index[0]
		j = index[1]
		if (0 <= i < len(array)) and (0 <= j < len(array[i])):
			adj.append( (i,j) )

	return adj

# dado uma matriz, retorna os indices adjacentes diagonais de um indice
def diag_adjacents(array, index):
	I = index[0]
	J = index[1]
	adj = []

	diags = [
		(I-1, J-1),
		(I-1, J+1),
		(I+1, J-1),
		(I+1, J+1)
	]

	for index in diags:
		i = index[0]
		j = index[1]
		if (0 <= i < len(array)) and (0 <= j < len(array[i])):
			adj.append( (i,j) )

	return adj

# retorna um nome para um no, de acordo com as coordenadas no mapa (ou matriz) que representa
def node_name(array, index):
	return str(index[0])+':'+str(index[1])

# dado uma matriz que representa uma mapa, retorna um grafo que representa tal mapa
def create_graph(map_array):
	
	WEIGHT_SIDE = 1
	WEIGHT_DIAG = sqrt(2)

	G = Graph()

	# inserindo nos no grafo
	for i, row in enumerate(map_array):
		for j, value in enumerate(row):

			# '-' = nao eh um no
			# '*' = no normal
			# '#' = no inicial
			# '$' = no final
			name = node_name( map_array, (i,j) )

			if value != '-':
				G.insert_node(name)

			if value == '#':
				G.set_start(name)
			elif value == '$':
				G.set_end(name)

	# inserindo arestas no gafo
	for i, row in enumerate(map_array):
		for j, value in enumerate(row):

			if value != '-':
				for a in side_adjacents(map_array, (i,j)):
					ai = a[0]
					aj = a[1]
					if map_array[ai][aj] != '-':
						# print(map_array[ai][aj])
						G.insert_arc(node_name(map_array, (i,j)), node_name(map_array, a), WEIGHT_SIDE)

				for a in diag_adjacents( map_array, (i,j) ):
					ai = a[0]
					aj = a[1]
					if map_array[ai][aj] != '-':
						# print(map_array[ai][aj])
						G.insert_arc(node_name(map_array, (i,j)), node_name(map_array, a), WEIGHT_DIAG)

	return G