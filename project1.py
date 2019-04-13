from src.graph import Graph
from src.map_parser import read_filemap, create_graph
import json

def test():

	arr = read_filemap('maps/map1.txt')

	grafo = create_graph(arr)

	print(json.dumps(grafo.struct, indent=2))
	print(grafo.start)
	print(grafo.end)

if __name__ == '__main__':
	test()