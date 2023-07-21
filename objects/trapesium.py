from models.vertex import Vertex
from models.object import Object

VERT_A = Vertex(-10, -20, 10)
VERT_B = Vertex(10, -20, 10)
VERT_C = Vertex(7, 20, 10)
VERT_D = Vertex(-7, 20, 10)
VERT_E = Vertex(-10, -20, 10)
VERT_F = Vertex(10, -20, -10)
VERT_G = Vertex(7, 20, -10)
VERT_H = Vertex(-7, 20, -10)

trapezium = Object([VERT_A, VERT_B, VERT_C, VERT_D, VERT_E, VERT_F, VERT_G, VERT_H], [
    [1, 0, 4, 5],
    [7, 4, 0, 3],
    [7, 3, 2, 6],
    [2, 1, 5, 6],
    [3, 5, 1, 3],
    [6, 5, 4, 7]
])
