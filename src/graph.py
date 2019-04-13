from math import sqrt

class Graph(object):

	def __init__(self):
		self.struct = dict()
		self.start = ''
		self.end = ''

	def insert_node(self, node_name):
		if node_name in self.struct.keys():
			print("ERRO: Nó já existe no grafo.")

		self.struct.update( {node_name: []} )

	def insert_arc(self, source, dest, weight):

		if source not in self.struct.keys():
			print("ERRO: Nó de origem "+source+" não existe no grafo.")
			return
		if dest not in self.struct.keys():
			print("ERRO: Nó de destino "+dest+" não existe no grafo.")
			return
		if (dest, 1) in self.struct[source] or (dest, sqrt(2)) in self.struct[source]:
			print("ERRO: Aresta ("+source+","+dest+") já existe no grafo.")
			return

		arc = (dest, weight)
		self.struct[source].append(arc)

	def set_start(self, node_name):
		self.start = node_name

	def set_end(self, node_name):
		self.end = node_name

	def find_path():
		pass

	def breadth_first():
		pass

	def depth_first():
		pass

	def best_first():
		pass

	def a_star():
		pass