from display import *
from draw import *
from parser import *
from matrix import *
import math

screen = new_screen()
color = [ 0, 0, 0 ]
edges = []
polygons = []
transform = new_matrix()
ident(transform)
csstack=[]
csstack.append(transform)

parse_file( 'script', edges, polygons, csstack, screen, color )
screen = new_screen()
edges = []
polygons = []
transform = new_matrix()
ident(transform)
csstack=[]
csstack.append(transform)
parse_file( 'domo', edges, polygons, csstack, screen, color )
