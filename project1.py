from src.graph import Graph
from src.map_parser import read_filemap, create_graph
from src.interface import MapInterface
import time
import json

def main():
	map_array = read_filemap('maps/map1.txt')

	#
	grafo = create_graph(map_array)
	if grafo == None:
		return
	print( 'Caminho entre '+grafo.start_node+' e '+grafo.end_node+':' )

	#
	gui_map = MapInterface(map_array)

	
	start_time = time.time()
	path_dfs = grafo.depth_first(grafo.start_node, grafo.end_node)[::-1] 
	dfs_time = time.time() - start_time
	
	print("Busca em Profundidade:")
	print("Tempo de Execução: "+str(dfs_time))
	print(path_dfs)
	gui_map.show_path(path_dfs)

	#
	start_time = time.time()
	path_bfs = grafo.breadth_first(grafo.start_node, grafo.end_node)
	bfs_time = time.time() - start_time
	
	print("Busca em Largura:")
	print("Tempo de Execução: "+str(bfs_time))
	print(path_bfs)
	gui_map.show_path(path_bfs)

	#
	start_time = time.time()
	path_bestfirst = grafo.best_first(grafo.start_node, grafo.end_node)
	bestfirst_time = time.time() - start_time
	
	print("Busca Best-First (algoritmo guloso):")
	print("Tempo de Execução: "+str(bestfirst_time))
	print(path_bestfirst)
	gui_map.show_path(path_bestfirst)

	#
	start_time = time.time()
	path_astar = grafo.a_star(grafo.start_node, grafo.end_node)
	astar_time = time.time() - start_time

	print("Busca A*:")
	print("Tempo de Execução: "+str(astar_time))
	print(path_astar)
	gui_map.show_path(path_astar)

if __name__ == '__main__':
	main()
