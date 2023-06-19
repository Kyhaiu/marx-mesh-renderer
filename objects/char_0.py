from models.vertex import Vertex
from models.object import Object

# The model of 0
VERTEX_0 = Vertex(x=102, y=149, z=0, id=0)
VERTEX_1 = Vertex(x=9, y=149, z=0, id=1)
VERTEX_2 = Vertex(x=72, y=118, z=0, id=2)
VERTEX_3 = Vertex(x=40, y=118, z=0, id=3)
VERTEX_4 = Vertex(x=72, y=41, z=0, id=4)
VERTEX_5 = Vertex(x=40, y=41, z=0, id=5)
VERTEX_6 = Vertex(x=102, y=10, z=0, id=6)
VERTEX_7 = Vertex(x=9, y=10, z=0, id=7)
VERTEX_8 = Vertex(x=102+20, y=149+20, z=1, id=8)
VERTEX_9 = Vertex(x=9+20, y=149+20, z=1, id=9)
VERTEX_10 = Vertex(x=72+20, y=118+20, z=1, id=10)
VERTEX_11 = Vertex(x=40+20, y=118+20, z=1, id=11)
VERTEX_12 = Vertex(x=72+20, y=41+20, z=1, id=12)
VERTEX_13 = Vertex(x=40+20, y=41+20, z=1, id=13)
VERTEX_14 = Vertex(x=102+20, y=10+20, z=1, id=14)
VERTEX_15 = Vertex(x=9+20, y=10+20, z=1, id=15)

zero = Object([
    VERTEX_0, VERTEX_1, VERTEX_2, VERTEX_3, VERTEX_4, VERTEX_5, VERTEX_6, VERTEX_7,
    VERTEX_8, VERTEX_9, VERTEX_10, VERTEX_11, VERTEX_12, VERTEX_13, VERTEX_14, VERTEX_15
], [
    [0, 1, 7, 6],
    [2, 3, 5, 4],
    [8, 14, 15, 9],
    [11, 10, 12, 13],
    [1, 9, 15, 7],
    [8, 9, 1, 0],
    [8, 0, 6, 14],
    [6, 7, 15, 14],
    [3, 11, 13, 5],
    [4, 5, 13, 12],
    [4, 12, 10, 2],
    [3, 2, 10, 11]
])

# v 102 149 0
# v 9 149 0
# v 72 118 0
# v 40 118 0
# v 72 41 0
# v 40 41 0
# v 102 10 0
# v 9 10 0
# v 102 149 1
# v 9 149 1
# v 72 118 1
# v 40 118 1
# v 72 41 1
# v 40 41 1
# v 102 10 1
# v 9 10 1

# f 1 2 8 7
# f 3 4 6 5
# f 9 15 16 10
# f 12 11 13 14
# f 2 10 16 8
# f 9 10 2 1
# f 9 1 7 15
# f 7 8 16 15
# f 4 12 14 6
# f 5 6 14 13
# f 5 13 11 3
# f 4 3 11 12
