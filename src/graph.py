from math import sqrt

class Graph(object):

	def __init__(self):
		self.struct = dict()
		self.start_node = ''
		self.end_node   = ''

	def insert_node(self, node_name):
		# checando por argumentos invalidos
		if node_name in self.struct.keys():
			print("ERRO: Nó já existe no grafo.")

		self.struct.update( {node_name: []} )

	def insert_arc(self, source, dest, weight):

		# checando por argumentos invalidos
		if source not in self.struct.keys():
			print("ERRO: Nó de origem "+source+" não existe no grafo.")
			return
		
		if dest not in self.struct.keys():
			print("ERRO: Nó de destino "+dest+" não existe no grafo.")
			return
		
		if ( (dest, 1) in self.struct[source] or
		     (dest, sqrt(2)) in self.struct[source] ):
			
			print("ERRO: Aresta ("+source+","+dest+") já existe no grafo.")
			return

		arc = (dest, weight)
		self.struct[source].append(arc)

	# retorna um nome para um no, de acordo com as coordenadas no mapa
	# (ou matriz) que representa
	def node_name(self, array, index):
		return '('+str(index[0])+', '+str(index[1])+')'

	def set_start(self, node_name):
		self.start_node = node_name

	def set_end(self, node_name):
		self.end_node = node_name

	def depth_first(self, start, end, path=None, visited=[]):
		#####
		if path is None:
			path = []

		visited.append(start)

		####
		if start == end:
			path.append(start)
			return path

		####
		node_edges = self.struct[start]
		for edge in node_edges:
			dest_node =	 edge[0]

			if dest_node not in visited:		
				
				subpath = self.depth_first(dest_node, end, path)

				if subpath != None:
					path.append(start)
					return path

	def breadth_first():
		pass

	def best_first():
		pass

	def a_star():
		pass