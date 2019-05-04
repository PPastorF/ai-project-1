from tkinter import *
from time import sleep
from ast import literal_eval

TILE_SIZE  = 40
TILE_COLOR = "white"

class MapInterface(object):

	def __init__(self, map_array):
		self.map_array = map_array
		self.size = ( len(map_array), len(map_array[0]) )

		#
		self.root = Tk()
		self.root.title("Projeto 1 - IA")
		self.canvas = Canvas(self.root, height=self.size[0]*TILE_SIZE, width=self.size[1]*TILE_SIZE)
		self.canvas.pack(expand=YES, fill=BOTH)

	def create_tile(self, coord, color):
		x_pos = coord[1]*TILE_SIZE
		y_pos = coord[0]*TILE_SIZE
		self.canvas.create_rectangle(x_pos,
									 y_pos,
									 x_pos+TILE_SIZE,
									 y_pos+TILE_SIZE,
									 fill=color)

	def show_path(self, path):

		for i in range(0,1):
			self.canvas.delete("all")

			for i, row in enumerate(self.map_array):
				for j, tile in enumerate(row):
					if tile == '*':
						tile_color = "white"
					if tile == '-':
						tile_color = "black"
					if tile == '#':
						tile_color = "blue"
					if tile == '$':
						tile_color = "green"
				
					self.create_tile((i,j), tile_color)

			for element in path:
				coord = literal_eval(element)
				self.create_tile(coord, "red")
				sleep(0.3)
				self.root.update_idletasks()
				self.root.update()

	def end(self):
		self.canvas.destroy()
		self.root.destroy()