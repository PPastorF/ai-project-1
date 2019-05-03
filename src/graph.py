from math import sqrt
from ast import literal_eval
from src.tools import *

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

	def depth_first(self, start, end, path=None, visited=None):
		#####
		if path is None:
			path = []

		if visited is None:
			visited = []

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
				
				subpath = self.depth_first(dest_node, end, path, visited)

				if subpath != None:
					path.append(start)
					return path

	def breadth_first(self, start, end):
		queue = [[start]]
		visited = []
		####
		while queue:
			path = queue.pop(0)

			####
			node = path[-1]
			
			if node in visited:
				continue

			print(node)
			if node == end:
				return path

			####
			node_edges = self.struct[node]
			for edge in node_edges:
				dest_node = edge[0]

				enqueue = list(path)
				enqueue.append(dest_node)

				queue.append(enqueue)

			visited.append(node)

	def best_first(self, start, end):
		###
		node_data  = {}
		open_nodes = []
		path       = []
		done 	   = []
		found = False

		###
		h = euclidian_distance(start, end)
		start_node = {
			start: {
				"h": h,
				"predecessor": None
			}
		}

		open_nodes.append( (start, h) )
		node_data.update(start_node)

		###
		while open_nodes:
			###
			open_nodes.sort(key=lambda tup: tup[1])
			open_nodes = open_nodes[::-1]
			current_node = open_nodes.pop(0)[0]

			if current_node == end:
				found = True
				break

			if current_node in done:
				continue

			dist = euclidian_distance(current_node, end)

			###
			node_edges = self.struct[current_node]
			for edge in node_edges:
				dest_node   = edge[0]
				edge_weight = edge[1]

				if dest_node in done:
					continue

				if dest_node not in open_nodes:
					open_nodes.append( (dest_node, h) )

				h = dist + edge_weight

				###
				adjacent = {
					dest_node: {
						"h": h,
						"predecessor": current_node		
					}
				}

				###
				if dest_node not in node_data.keys():
					node_data.update(adjacent)
				elif h < node_data[dest_node]['h']:
					node_data[dest_node] = adjacent[dest_node]

			done.append(current_node)

		###
		if found:
			path.append(end)
			current_node = node_data[end]

			while current_node['predecessor'] != None:
				pred = current_node['predecessor']
				path.append(pred)
				current_node = node_data[pred]

			return path[::-1]
		
		else:
			return None

	def a_star(self, start, end):
		###
		node_data  = {}
		open_nodes = []
		path       = []
		done 	   = []
		found = False

		###
		g = 0
		f = g + euclidian_distance(start, end)
		start_node = {
			start: {
				"g": g,
				"f": f,
				"predecessor": None
			}
		}

		open_nodes.append( (start, f) )
		node_data.update(start_node)

		###
		while open_nodes:
			###
			open_nodes.sort(key=lambda tup: tup[1])
			open_nodes = open_nodes[::-1]
			current_node = open_nodes.pop(0)[0]

			if current_node == end:
				found = True
				break

			if current_node in done:
				continue

			h = euclidian_distance(current_node, end)

			###
			node_edges = self.struct[current_node]
			for edge in node_edges:
				dest_node   = edge[0]
				edge_weight = edge[1]

				if dest_node in done:
					continue

				if dest_node not in open_nodes:
					open_nodes.append( (dest_node, f) )

				g = node_data[current_node]['g'] + edge_weight
				f = g + h


				###
				adjacent = {
					dest_node: {
						"g": g,
						"f": f,
						"predecessor": current_node		
					}
				}

				###
				if dest_node not in node_data.keys():
					node_data.update(adjacent)
				elif f < node_data[dest_node]['f']:
					node_data[dest_node] = adjacent[dest_node]

			done.append(current_node)

		###
		if found:
			path.append(end)
			current_node = node_data[end]

			while current_node['predecessor'] != None:
				pred = current_node['predecessor']
				path.append(pred)
				current_node = node_data[pred]

			return path[::-1]
		
		else:
			return None