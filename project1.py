from src.graph import Graph
from src.map_parser import read_filemap, create_graph
import json

def main():
	arr = read_filemap('maps/map1.txt')
	grafo = create_graph(arr)

def test():

	arr = read_filemap('maps/map1.txt')

	arr = [
		['#', '*', '*'],
		['*', '-', '-'],
		['*', '*', '$']
	]

	grafo = create_graph(arr)


	# print(json.dumps(grafo.struct, indent=2))
	print('Caminho entre '+grafo.start_node+' e '+grafo.end_node+':')
	print("DFS:")

	print( grafo.depth_first(grafo.start_node, grafo.end_node)[::-1] )

if __name__ == '__main__':
	test()