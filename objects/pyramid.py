from models.vertex import Vertex
from models.object import Object

# Create vertices
VERT_A = Vertex(30, 2, 25)
VERT_B = Vertex(35, 4, 20)
VERT_C = Vertex(25, 3, 18)
VERT_D = Vertex(20, 1, 23)
VERT_E = Vertex(30, 10, 22.5)

pyramid = Object([VERT_A, VERT_B, VERT_C, VERT_D, VERT_E], [
    [0, 1, 4],
    [1, 2, 4],
    [2, 3, 4],
    [3, 0, 4],
    [0, 3, 2, 1]
])

# v 30 2 25
# v 35 4 20
# v 25 3 18
# v 20 1 23
# v 30 10 22.5
# f 1 2 5
# f 2 3 5
# f 3 4 5
# f 4 1 5
# f 1 4 3 2
