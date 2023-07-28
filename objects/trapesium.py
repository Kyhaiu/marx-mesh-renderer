from models.vertex import Vertex
from models.object import Object

VERT_A = Vertex(-10, -20, 10)
VERT_B = Vertex(10, -20, 10)
VERT_C = Vertex(7, 20, 10)
VERT_D = Vertex(-7, 20, 10)
VERT_E = Vertex(-10, -20, -10)
VERT_F = Vertex(10, -20, -10)
VERT_G = Vertex(7, 20, -10)
VERT_H = Vertex(-7, 20, -10)

trapezium = Object([VERT_A, VERT_B, VERT_C, VERT_D, VERT_E, VERT_F, VERT_G, VERT_H], [
    [0, 1, 2, 3],
    [3, 7, 4, 0],
    [3, 2, 6, 7],
    [1, 5, 6, 2],
    [0, 4, 5, 1],
    [5, 4, 7, 6]
])


# v -20 -30 20
# v 20 -30 20
# v 14 30 20
# v -14 30 20
# v -10 -20 -10
# v 10 -20 -10
# v 7 20 -10
# v -7 20 -10

# f 1 2 3 4
# f 4 8 5 1
# f 4 3 7 8
# f 2 6 7 3
# f 1 5 6 2
# f 6 5 8 7
