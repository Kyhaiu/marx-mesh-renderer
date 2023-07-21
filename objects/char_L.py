from models.vertex import Vertex
from models.object import Object

# The model of L
VERTEX_1 = Vertex(x=1.0, y=1.0, z=-0.5, id=0)
VERTEX_2 = Vertex(x=1.3333333333333333, y=1.0, z=-0.5, id=1)
VERTEX_3 = Vertex(x=1.3333333333333333, y=1.7785714285714285, z=-0.5, id=2)
VERTEX_4 = Vertex(x=2.0, y=1.7785714285714285, z=-0.5, id=3)
VERTEX_5 = Vertex(x=1.0, y=2.0, z=-0.5, id=4)
VERTEX_6 = Vertex(x=2.0, y=2.0, z=-0.5, id=5)
VERTEX_7 = Vertex(x=-1.0, y=0.0, z=0.5, id=6)
VERTEX_8 = Vertex(x=-0.6666666666666667, y=0.0, z=0.5, id=7)
VERTEX_9 = Vertex(x=-0.6666666666666667, y=0.7785714285714286, z=0.5, id=8)
VERTEX_10 = Vertex(x=0.0, y=0.7785714285714286, z=0.5, id=9)
VERTEX_11 = Vertex(x=-1.0, y=1.0, z=0.5, id=10)
VERTEX_12 = Vertex(x=0.0, y=1.0, z=0.5, id=11)

L = Object(
    vertices=[
        VERTEX_1,
        VERTEX_2,
        VERTEX_3,
        VERTEX_4,
        VERTEX_5,
        VERTEX_6,
        VERTEX_7,
        VERTEX_8,
        VERTEX_9,
        VERTEX_10,
        VERTEX_11,
        VERTEX_12,
    ],
    faces=[
        [6, 7, 8, 9, 11, 10],
        [0, 4, 5, 3, 2, 1],
        [6, 10, 4, 0],
        [6, 0, 1, 7],
        [7, 1, 2, 8],
        [8, 2, 3, 9],
        [9, 3, 5, 11],
        [11, 5, 4, 10],
    ],
)

# v 1.0 1.0 -0.5
# v 1.3333333333333333 1.0 -0.5
# v 1.3333333333333333 1.7785714285714285 -0.5
# v 2.0 1.7785714285714285 -0.5
# v 1.0 2.0 -0.5
# v 2.0 2.0 -0.5
# v -1.0 0.0 0.5
# v -0.6666666666666667 0.0 0.5
# v -0.6666666666666667 0.7785714285714286 0.5
# v 0.0 0.7785714285714286 0.5
# v -1.0 1.0 0.5
# v 0.0 1.0 0.5


# f 7 8 9 10 12 11
# f 1 5 6 4 3 2

# f 7 11 5 1
# f 7 1 2 8
# f 8 2 3 9
# f 9 3 4 10
# f 10 4 6 12
# f 12 6 5 11
