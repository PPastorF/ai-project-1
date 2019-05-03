from src.graph import Graph
from src.map_parser import read_filemap, create_graph
import json

def main():
	arr = read_filemap('maps/map1.txt')

	arr = [
		['#', '*', '*'],
		['*', '*', '*'],
		['*', '*', '$']
	]

	grafo = create_graph(arr)
	if grafo == None:
		return

	print( 'Caminho entre '+grafo.start_node+' e '+grafo.end_node+':' )
	print( "DFS:" )
	print( grafo.depth_first(grafo.start_node, grafo.end_node)[::-1] )

	print( "BFS:" )
	print( grafo.breadth_first(grafo.start_node, grafo.end_node) )
	
	print( "A STAR:" )
	print( grafo.a_star(grafo.start_node, grafo.end_node) )

	print( "BEST FIRST:" )
	print( grafo.best_first(grafo.start_node, grafo.end_node) )

if __name__ == '__main__':
	main()